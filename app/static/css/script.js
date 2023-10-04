document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM Content Loaded");
    const reviewCards = document.querySelectorAll('.review-card');  // This line is added

    setTimeout(function() {
        const splash = document.querySelector(".splash-screen");
        splash.style.display = 'none';
        document.body.style.overflow = 'auto'; // Enable scrolling again
    }, 3000); // 3 seconds (the total time of both animations)

    reviewCards.forEach(card => {
        card.addEventListener('click', function() {
            const isActive = card.classList.contains('active');
            console.log("Card clicked");

            reviewCards.forEach(innerCard => innerCard.classList.remove('active'));
            document.querySelector('.content-wrapper').classList.remove('blurred');

            if (!isActive) {
                card.classList.add('active');
                document.querySelector('.content-wrapper').classList.add('blurred');
            }
        });
    });

    document.body.addEventListener('click', function(e) {
        if (!e.target.closest('.review-card')) {
            reviewCards.forEach(card => card.classList.remove('active'));
            document.querySelector('.content-wrapper').classList.remove('blurred');
        }
    }, true);
});
