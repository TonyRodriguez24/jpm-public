$(document).ready(function () {
    emailjs.init('PWX9hwKjZs3ZUe5V3'),
        $('#contact-form').on('submit', function (e) {
            e.preventDefault(),
                emailjs
                    .sendForm(
                        'service_88k82ug',
                        'template_llnmo1o',
                        '#contact-form',
                    )
                    .then(
                        (e) => {
                            console.log('SUCCESS!', e.status, e.text),
                                $('#contact-form').hide(),
                                $('#form-success-container').show()
                        },
                        (e) => {
                            console.log('FAILED...', e),
                                alert(
                                    'There was an error sending your message.',
                                )
                        },
                    )
        })
})
