console.log('cart.js loaded');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showToast(message, isError = false) {
    const toast = document.getElementById('cartToast');
    const toastBody = toast.querySelector('.toast-body');
    const toastHeader = toast.querySelector('.toast-header strong');
    
    if (isError) {
        toast.classList.add('bg-danger', 'text-white');
        toastHeader.textContent = 'خطأ!';
    } else {
        toast.classList.remove('bg-danger', 'text-white');
        toastHeader.textContent = 'تم بنجاح!';
    }
    
    toastBody.textContent = message;
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
}

function addToCart(button) {
    try {
        // الحصول على البيانات من الزر
        const productId = button.dataset.productId;
        const productName = button.dataset.productName;
        
        console.log('Adding to cart:', { productId, productName }); // للتصحيح
        
        // التحقق من وجود البيانات
        if (!productId || !productName) {
            showToast('خطأ في بيانات المنتج', true);
            return;
        }

        const csrftoken = getCookie('csrftoken');
        
        // تعطيل الزر أثناء الطلب
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري الإضافة...';
        
        fetch(`/orders/cart/add/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            credentials: 'same-origin'
        })
        .then(response => {
            if (!response.ok) {
                if (response.status === 403) {
                    throw new Error('يرجى تسجيل الدخول لإضافة منتجات إلى السلة');
                }
                throw new Error('حدث خطأ أثناء إضافة المنتج إلى السلة');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            showToast(`تمت إضافة ${productName} إلى السلة`);
        })
        .catch(error => {
            console.error('Error:', error);
            showToast(error.message, true);
        })
        .finally(() => {
            // إعادة تفعيل الزر
            button.disabled = false;
            button.innerHTML = '<i class="fas fa-shopping-cart"></i> أضف للسلة';
        });
    } catch (error) {
        console.error('Error in addToCart:', error);
        showToast('حدث خطأ غير متوقع', true);
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-shopping-cart"></i> أضف للسلة';
    }
}
