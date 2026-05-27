// static/js/footer.js

class MotionFooter {
    constructor() {
        this.backToTopBtn = document.getElementById('backToTop');
        this.newsletterForm = document.getElementById('newsletterForm');
        this.socialIcons = document.querySelectorAll('.social-icon');
        this.init();
    }

    init() {
        this.handleBackToTop();
        this.handleNewsletter();
        this.handleSocialLinks();
        this.addScrollReveal();
        this.handleDynamicYear();
        this.addParticleEffect();
        this.addSmoothScrolling();
    }

    handleBackToTop() {
        if (this.backToTopBtn) {
            this.backToTopBtn.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            // Show/hide back to top button with animation
            window.addEventListener('scroll', () => {
                if (window.scrollY > 500) {
                    this.backToTopBtn.style.opacity = '1';
                    this.backToTopBtn.style.visibility = 'visible';
                    this.backToTopBtn.style.transform = 'translateY(0)';
                } else {
                    this.backToTopBtn.style.opacity = '0';
                    this.backToTopBtn.style.visibility = 'hidden';
                    this.backToTopBtn.style.transform = 'translateY(20px)';
                }
            });
        }
    }

    handleSocialLinks() {
        if (this.socialIcons.length > 0) {
            this.socialIcons.forEach(icon => {
                icon.addEventListener('click', (e) => {
                    const platform = this.getSocialPlatform(icon);
                    this.showNotification(`🎬 Visiting ${platform} page...`, 'success');
                    
                    // Optional: Track social media clicks in analytics
                    console.log(`Social media clicked: ${platform} - ${icon.href}`);
                });
            });
        }
    }

    getSocialPlatform(icon) {
        const href = icon.href.toLowerCase();
        if (href.includes('facebook')) return 'Facebook';
        if (href.includes('twitter')) return 'Twitter';
        if (href.includes('instagram')) return 'Instagram';
        if (href.includes('youtube')) return 'YouTube';
        if (href.includes('dribbble')) return 'Dribbble';
        return 'Social Media';
    }

    handleNewsletter() {
        if (this.newsletterForm) {
            this.newsletterForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                const emailInput = this.newsletterForm.querySelector('input[type="email"]');
                const email = emailInput.value;
                
                if (!this.validateEmail(email)) {
                    this.showNotification('Please enter a valid email address!', 'error');
                    return;
                }
                
                // Show loading state
                const submitBtn = this.newsletterForm.querySelector('.subscribe-btn');
                const originalHTML = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                submitBtn.disabled = true;
                
                // Simulate API call
                setTimeout(() => {
                    this.showNotification('Thanks for subscribing! 🎉', 'success');
                    emailInput.value = '';
                    submitBtn.innerHTML = originalHTML;
                    submitBtn.disabled = false;
                    
                    // Store in localStorage
                    const subscribers = JSON.parse(localStorage.getItem('subscribers') || '[]');
                    if (!subscribers.includes(email)) {
                        subscribers.push(email);
                        localStorage.setItem('subscribers', JSON.stringify(subscribers));
                    }
                }, 1000);
            });
        }
    }

    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    showNotification(message, type) {
        // Remove existing notification
        const existingNotification = document.querySelector('.footer-notification');
        if (existingNotification) existingNotification.remove();
        
        const notification = document.createElement('div');
        notification.className = `footer-notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
                <span>${message}</span>
            </div>
        `;
        
        notification.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px 20px;
            border-radius: 10px;
            z-index: 10000;
            animation: slideInRight 0.3s ease;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
            font-family: 'Inter', sans-serif;
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    addScrollReveal() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.footer-section').forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(30px)';
            section.style.transition = 'all 0.6s ease';
            observer.observe(section);
        });
    }

    handleDynamicYear() {
        const yearElement = document.getElementById('currentYear');
        if (yearElement) {
            const currentYear = new Date().getFullYear();
            yearElement.textContent = currentYear;
        }
    }

    addParticleEffect() {
        const particlesContainer = document.querySelector('.footer-particles');
        if (particlesContainer) {
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.style.position = 'absolute';
                particle.style.width = '2px';
                particle.style.height = '2px';
                particle.style.background = 'rgba(102, 126, 234, 0.5)';
                particle.style.borderRadius = '50%';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animation = `floatParticle ${5 + Math.random() * 10}s linear infinite`;
                particlesContainer.appendChild(particle);
            }
        }
    }

    addSmoothScrolling() {
        document.querySelectorAll('.footer-links a, .footer-legal a, .back-to-top').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href && href.startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
        });
    }
}

// Add CSS animations
const styleSheet = document.createElement("style");
styleSheet.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    @keyframes floatParticle {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(styleSheet);

// Initialize footer when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new MotionFooter();
});

// Parallax effect on footer glow
document.addEventListener('mousemove', (e) => {
    const glow = document.querySelector('.footer-glow');
    if (glow) {
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        glow.style.transform = `translate(${mouseX * 20}px, ${mouseY * 20}px)`;
    }
});