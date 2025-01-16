const cards = document.querySelectorAll(".custom-card");
let playing = false; // Shared state for animation

cards.forEach((card) => {
    card.addEventListener("click", function () {
        if (playing) return;

        playing = true; // Lock animation state
        anime({
            targets: card,
            scale: [{ value: 1 }, { value: 1.2 }, { value: 1, delay: 250 }],
            rotateY: { value: '+=180', delay: 200 },
            easing: "easeInOutSine",
            duration: 400,
            complete: function () {
                playing = false; // Unlock when animation completes
            },
        });
    });
});
