//Animation for the noodle startup
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM Content Loaded");
    const reviewCards = document.querySelectorAll('.review-card'); 

    setTimeout(function() {
        const splash = document.querySelector(".splash-screen");
        splash.style.display = 'none';
        document.body.style.overflow = 'auto'; // Enable scrolling again
    }, 3000); // 3 seconds (the total time of both animations)
});
