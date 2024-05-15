document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

        var formData = {
            firstname: $("#firstname").val(),
            lastname: $("#lastname").val(),
            email: $("#email").val(),
            phone: $("#phone").val(),
            password: $("#password").val()
        };

        $.ajax({
            type: "POST",
            url: "http://localhost:8000/register/user",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function(response) {
                window.location.href = '/chat';
            },
            error: function(xhr, status, error) {
                if (xhr.status === 400) {
                    $("#errorMessage").text(xhr.responseJSON.detail);
                    $("#errorModal").modal("show");
                } else {
                    console.error("Registration failed:", error);
                }
            }
    });
});