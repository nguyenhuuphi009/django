// File: index.js

document.addEventListener('DOMContentLoaded', (event) => {
    const loginForm = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Kiểm tra xem các trường có bị để trống không
        if (usernameInput.value.trim() === '' || passwordInput.value.trim() === '') {
            alert('Lỗi: Tên đăng nhập và mật khẩu không được để trống.');
            return; // Dừng việc thực thi các lệnh tiếp theo
        }

        // Nếu các trường không trống, tiếp tục kiểm tra mật khẩu
        const isConfirmed = confirm('Bạn có chắc chắn muốn đăng nhập không?');

        if (isConfirmed) {
            const password = passwordInput.value;
            const passwordRegex = /^[a-zA-Z0-9]+$/;

            if (passwordRegex.test(password)) {
                // Mật khẩu hợp lệ
                alert('Đăng nhập thành công! Mật khẩu hợp lệ.');

                // Gửi form đi
                loginForm.submit();
            } else {
                // Mật khẩu không hợp lệ
                alert('Lỗi: Mật khẩu chỉ được chứa ký tự và số.');
                usernameInput.value = '';
                passwordInput.value = '';
            }
        } else {
            // Người dùng đã hủy đăng nhập
            console.log('Người dùng đã hủy đăng nhập.');
        }
    });
});