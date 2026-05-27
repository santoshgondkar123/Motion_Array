// base.js - Additional JavaScript for base.html

// GSAP Scroll Animations
gsap.registerPlugin(ScrollTrigger);

// Animate elements on scroll
function initScrollAnimations() {
    // Fade up animation
    gsap.utils.toArray('.project-card, .skill-card, .contact-info, .contact-form').forEach(element => {
        gsap.from(element, {
            scrollTrigger: {
                trigger: element,
                start: 'top 85%',
                toggleActions: 'play none none reverse'
            },
            opacity: 0,
            y: 50,
            duration: 0.8,
            ease: 'power3.out'
        });
    });
}

// Parallax effect on hero section
function initParallax() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero-section');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });
}

// Typing effect for hero title (optional)
function initTypingEffect() {
    const titleElement = document.querySelector('.hero-title .title-line:first-child');
    if (titleElement && titleElement.innerText === 'Welcome') {
        const originalText = titleElement.innerText;
        titleElement.innerText = '';
        let i = 0;
        const typeInterval = setInterval(() => {
            if (i < originalText.length) {
                titleElement.innerText += originalText.charAt(i);
                i++;
            } else {
                clearInterval(typeInterval);
            }
        }, 100);
    }
}

// Smooth reveal for stat numbers
function initStatCounter() {
    const stats = document.querySelectorAll('.stat-number');
    
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statElement = entry.target;
                const targetNumber = parseInt(statElement.innerText);
                let currentNumber = 0;
                const increment = targetNumber / 50;
                
                const updateNumber = () => {
                    if (currentNumber < targetNumber) {
                        currentNumber += increment;
                        statElement.innerText = Math.floor(currentNumber) + '+';
                        requestAnimationFrame(updateNumber);
                    } else {
                        statElement.innerText = targetNumber + '+';
                    }
                };
                
                updateNumber();
                observer.unobserve(statElement);
            }
        });
    }, observerOptions);
    
    stats.forEach(stat => observer.observe(stat));
}

// Add hover effect to project cards
function initCardHover() {
    const cards = document.querySelectorAll('.project-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                scale: 1.02,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                scale: 1,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
    });
}

// Initialize all functions
document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initParallax();
    initStatCounter();
    initCardHover();
    
    // Typing effect (optional - uncomment if wanted)
    // initTypingEffect();
});

// Handle window resize
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // Refresh ScrollTrigger on resize
        ScrollTrigger.refresh();
    }, 250);
});