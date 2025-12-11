/**
 * Modern Academic Portfolio - Interactive Features
 * ================================================
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all features
    initNavbar();
    initSmoothScroll();
    initScrollAnimations();
    initScrollProgress();
    initBackToTop();
    initMeteorShower();
});

/**
 * Navbar scroll behavior
 */
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (!navbar) return;

    // Add scrolled class on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile menu toggle
    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            navToggle.classList.toggle('active');
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });
    }
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const navbarHeight = document.querySelector('.navbar')?.offsetHeight || 0;
                const targetPosition = targetElement.offsetTop - navbarHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Scroll-based reveal animations
 */
function initScrollAnimations() {
    const sections = document.querySelectorAll('.section');
    const cards = document.querySelectorAll('.education-item, .experience-item, .project-item, .research-item, .skill-category');

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Animate child cards with stagger effect
                const childCards = entry.target.querySelectorAll('.education-item, .experience-item, .project-item, .research-item, .skill-category');
                childCards.forEach((card, index) => {
                    setTimeout(() => {
                        card.classList.add('fade-in');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Observe individual cards that might be outside sections
    cards.forEach(card => {
        observer.observe(card);
    });
}

/**
 * Scroll progress indicator
 */
function initScrollProgress() {
    const progressBar = document.querySelector('.scroll-progress');
    if (!progressBar) return;

    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = `${progress}%`;
    });
}

/**
 * Back to top button
 */
function initBackToTop() {
    const backToTop = document.querySelector('.back-to-top');
    if (!backToTop) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Typing effect (optional - for hero subtitle)
 */
function initTypingEffect(element, texts, speed = 100) {
    if (!element) return;

    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
        const currentText = texts[textIndex];

        if (isDeleting) {
            element.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
        } else {
            element.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
        }

        element.classList.add('typing-cursor');

        let typeSpeed = speed;

        if (isDeleting) {
            typeSpeed /= 2;
        }

        if (!isDeleting && charIndex === currentText.length) {
            typeSpeed = 2000; // Pause at end
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500; // Pause before new text
        }

        setTimeout(type, typeSpeed);
    }

    type();
}

/**
 * Add parallax effect to hero (subtle)
 */
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    if (hero && window.scrollY < window.innerHeight) {
        const scrolled = window.scrollY;
        hero.style.transform = `translateY(${scrolled * 0.3}px)`;
        hero.style.opacity = 1 - (scrolled / window.innerHeight) * 0.5;
    }
});

/**
 * Meteor Shower Effect
 * Creates falling meteors from top-left to bottom-right
 */
function initMeteorShower() {
    // Create meteor shower container
    const meteorShower = document.createElement('div');
    meteorShower.className = 'meteor-shower';
    document.body.insertBefore(meteorShower, document.body.firstChild);

    // Meteor creation function
    function createMeteor() {
        const meteor = document.createElement('div');
        meteor.className = 'meteor';

        // Random starting position (full screen coverage)
        const startX = Math.random() * (window.innerWidth + 200) - 100;
        const startY = Math.random() * window.innerHeight * 0.5 - 150;

        // Random properties for variety
        const duration = 1.5 + Math.random() * 1.5; // 1.5-3 seconds
        const size = 0.5 + Math.random() * 0.8; // Scale variation
        const delay = Math.random() * 0.3;

        meteor.style.left = `${startX}px`;
        meteor.style.top = `${startY}px`;
        meteor.style.animationDuration = `${duration}s`;
        meteor.style.animationDelay = `${delay}s`;
        meteor.style.transform = `rotate(45deg) scale(${size})`;

        meteorShower.appendChild(meteor);

        // Remove meteor after animation completes
        setTimeout(() => {
            if (meteor.parentNode) {
                meteor.remove();
            }
        }, (duration + delay) * 1000 + 100);
    }

    // Create meteors at intervals (moderate frequency)
    function startMeteorShower() {
        // Initial burst of a few meteors
        for (let i = 0; i < 5; i++) {
            setTimeout(createMeteor, i * 300);
        }

        // Continue creating meteors at moderate intervals
        setInterval(() => {
            // Random chance to create 1-3 meteors
            const meteorCount = 1 + Math.floor(Math.random() * 3);
            for (let i = 0; i < meteorCount; i++) {
                setTimeout(createMeteor, i * 200);
            }
        }, 800 + Math.random() * 700); // Every 0.8-1.5 seconds
    }

    startMeteorShower();
}
