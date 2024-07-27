document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("landing-page").classList.add("visible");
    console.log("Document is ready");
});

// Essential Google Tag Manager
(function () {
    var gtmScript = document.createElement('script');
    gtmScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-2HYHDJVPGJ';
    gtmScript.async = true;
    document.head.appendChild(gtmScript);

    gtmScript.onload = function () {
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-2HYHDJVPGJ', {
            'optimize_id': 'OPT_CONTAINER_ID',
            'anonymize_ip': true,
            'allow_ad_personalization_signals': false,
            'send_page_view': false // Disable automatic page view tracking
        });
    };
})();

// Defer loading non-essential tags
window.addEventListener('load', function () {
    var nonEssentialScript = document.createElement('script');
    nonEssentialScript.src = 'https://www.googletagmanager.com/gtag/js?id=GT-NGPQ79NG';
    nonEssentialScript.async = true;
    document.head.appendChild(nonEssentialScript);

    nonEssentialScript.onload = function () {
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'GT-NGPQ79NG');
    };
});
