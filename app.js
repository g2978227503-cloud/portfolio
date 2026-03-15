/* ══════════════════════════════════════
   Goofy — Shared Scripts
   ══════════════════════════════════════ */

// ── Scramble Text Effect ──
const scrambleChars = '█▓▒░><+-_/\\{}[]';

class ScrambleText {
    constructor(el, isBody = false) {
        this.el = el;
        this.originalText = el.getAttribute('data-original') || el.innerText;
        this.textArray = this.originalText.split('');
        this.isAnimating = false;
        this.isBody = isBody;
        this.el.addEventListener('mouseenter', () => this.trigger());
        this.el.addEventListener('mouseleave', () => this.resolve());
    }

    trigger() {
        if (this.isAnimating) return;
        this.isAnimating = true;
        let iterations = 0;
        clearInterval(this.interval);
        this.interval = setInterval(() => {
            this.el.innerText = this.textArray.map((char, index) => {
                if (char === ' ') return ' ';
                if (index < iterations / 2) return this.originalText[index];
                if (this.isBody) {
                    return Math.random() > 0.5 ? char : ['▒', '░', '.', ':'][Math.floor(Math.random() * 4)];
                }
                return scrambleChars[Math.floor(Math.random() * scrambleChars.length)];
            }).join('');
            if (iterations >= this.originalText.length * 2) {
                clearInterval(this.interval);
                this.el.innerText = this.originalText;
                this.isAnimating = false;
            }
            iterations++;
        }, 30);
    }

    resolve() {
        clearInterval(this.interval);
        this.el.innerText = this.originalText;
        this.isAnimating = false;
    }
}

// ── Scroll Fade-in Observer ──
function initFadeIn() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
}

// ── Mobile Nav Toggle ──
function initMobileNav() {
    const hamburger = document.querySelector('.nav-hamburger');
    const mobileNav = document.querySelector('.mobile-nav');
    if (!hamburger || !mobileNav) return;

    hamburger.addEventListener('click', () => {
        mobileNav.classList.toggle('active');
        document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
    });

    mobileNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileNav.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

// ── Clock ──
function initClock() {
    const clockEl = document.getElementById('clock');
    if (!clockEl) return;
    function update() {
        const now = new Date();
        // Convert to Beijing Time (UTC+8)
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        const beijingTime = new Date(utc + (3600000 * 8));
        const timeStr = beijingTime.toISOString().substring(11, 19) + ' BJ';
        clockEl.innerText = timeStr;
    }
    setInterval(update, 1000);
    update();
}

// ── Init All ──
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.scramble-target').forEach(el => new ScrambleText(el, false));
    document.querySelectorAll('.scramble-target-body').forEach(el => new ScrambleText(el, true));
    initFadeIn();
    initMobileNav();
    initClock();

    // ── Work List Hover Preview ──
    const workRows = document.querySelectorAll('.work-row');
    let previewImg = document.createElement('img');
    previewImg.style.position = 'fixed';
    previewImg.style.pointerEvents = 'none';
    previewImg.style.opacity = '0';
    previewImg.style.transition = 'opacity 0.3s ease, transform 0.3s var(--transition)';
    previewImg.style.transform = 'translate(-50%, -50%) scale(0.9)';
    previewImg.style.zIndex = '100';
    previewImg.style.width = '30vw';
    previewImg.style.height = 'auto';
    previewImg.style.objectFit = 'cover';
    document.body.appendChild(previewImg);

    workRows.forEach(row => {
        row.addEventListener('mouseenter', (e) => {
            const previewUrl = row.getAttribute('data-preview');
            if (previewUrl) {
                previewImg.src = previewUrl;
                previewImg.style.opacity = '1';
                previewImg.style.transform = `translate(${e.clientX}px, ${e.clientY}px) scale(1)`;
            }
        });
        
        row.addEventListener('mousemove', (e) => {
            previewImg.style.transform = `translate(${e.clientX}px, ${e.clientY}px) scale(1)`;
        });

        row.addEventListener('mouseleave', () => {
            previewImg.style.opacity = '0';
            previewImg.style.transform = 'translate(-50%, -50%) scale(0.9)';
        });
    });
});
