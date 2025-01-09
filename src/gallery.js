document.addEventListener('DOMContentLoaded', () => {
    let e = { threshold: 0.1 },
        t = new IntersectionObserver((e, t) => {
            e.forEach((e) => {
                e.isIntersecting &&
                    (e.target.classList.add('fade-in'), t.unobserve(e.target))
            })
        }, e),
        n = (e) => {
            document.querySelectorAll(e).forEach((e) => {
                i(e) ? e.classList.add('fade-in') : t.observe(e)
            })
        },
        i = (e) => {
            let t = e.getBoundingClientRect()
            return (
                t.top >= 0 &&
                t.left >= 0 &&
                t.bottom <=
                    (window.innerHeight ||
                        document.documentElement.clientHeight) &&
                t.right <=
                    (window.innerWidth || document.documentElement.clientWidth)
            )
        }
    n('#entire-gallery img'), n('#gallery-container .gallery img')
})
