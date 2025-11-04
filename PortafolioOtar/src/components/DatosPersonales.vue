<script setup>
// IMPORTACIONES
import linkedin from '/src/assets/linkedin.png';
import instagram from '/src/assets/instagram.png';
import github from '/src/assets/github.png';
import resume from '/src/assets/resume.png';

const nombreOtar ='Otar Kebadze';
const descripcionOtar ='Técnico Universitario en Programación - UTN / FullStack MERN';
const residenciaOtar = 'Mendoza, Argentina';
const presentacionOtar = 'Apasionado por la tecnología y el desarrollo de software. Especializado en el stack MERN con enfoque en crear soluciones innovadoras y eficientes.';
const telefonoOtar = '+54 2657 41-54452';

// Datos para el v-for de contactos
const contactItems = [
    { icon: '📍', text: residenciaOtar },
    { icon: '📞', text: telefonoOtar }
];

const redesSocialesOtar = [
    {id:1, nombre:'Linkedin', src: linkedin, url:'https://www.linkedin.com'},
    {id:2, nombre:'Instagram', src: instagram, url:'https://www.instagram.com'},
    {id:3, nombre:'Github', src: github, url:'https://github.com'},
    {id:4, nombre:'CV', src: resume, url:'/cv.pdf'},
];
</script>

<template>
    <section class="hero-section">
        <div class="container">
            <div class="presentation-card">
                <div class="card-header">
                    <div class="title-container">
                        <h1 class="main-title">{{ nombreOtar }}</h1>
                        <div class="decoration-line"></div>
                        <p class="subtitle">Portafolio UTN San Rafael - Cohorte 2025</p>
                    </div>
                </div>
                
                <div class="card-content">
                    <div class="profile-info">
                        <h2 class="role">{{ descripcionOtar }}</h2>
                        <p class="description">{{ presentacionOtar }}</p>
                        
                        <div class="contact-info">
                            <div 
                                v-for="(contact, index) in contactItems" 
                                :key="index" 
                                class="contact-item"
                            >
                                <span class="contact-icon">{{ contact.icon }}</span>
                                <span>{{ contact.text }}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="social-section">
                        <h3 class="social-title">Conectemos</h3>
                        <div class="social-links">
                            <a 
                                v-for="red in redesSocialesOtar" 
                                :key="red.id" 
                                :href="red.url" 
                                class="social-link"
                                target="_blank"
                                rel="noopener noreferrer"
                                :title="red.nombre"
                            >
                                <img class="social-icon" :src="red.src" :alt="red.nombre" />
                                <span class="social-name">{{ red.nombre }}</span>
                            </a>
                        </div>
                    </div>
                </div>
                
                <div class="card-glow"></div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.hero-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    background: var(--color-background);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(163, 230, 53, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(163, 230, 53, 0.05) 0%, transparent 50%);
    pointer-events: none;
}

.container {
    max-width: 800px;
    width: 100%;
}

.presentation-card {
    background: var(--color-background-soft);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius-lg);
    padding: 3rem;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    transition: all var(--transition-smooth);
    box-shadow: var(--shadow-glow);
}

.presentation-card:hover {
    border-color: var(--color-primary);
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(163, 230, 53, 0.15);
}

.card-glow {
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(163, 230, 53, 0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity var(--transition-smooth);
    pointer-events: none;
}

.presentation-card:hover .card-glow {
    opacity: 1;
}

.card-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.main-title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-hover) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 1rem 0;
    font-weight: 700;
}

.decoration-line {
    width: 100px;
    height: 3px;
    background: linear-gradient(90deg, var(--color-primary), transparent);
    margin: 0 auto 1rem auto;
    border-radius: 2px;
}

.subtitle {
    color: var(--color-text);
    opacity: 0.8;
    font-size: 1.1rem;
    margin: 0;
}

.card-content {
    display: grid;
    gap: 2.5rem;
}

.profile-info {
    text-align: center;
}

.role {
    color: var(--color-heading);
    font-size: 1.4rem;
    margin: 0 0 1.5rem 0;
    font-weight: 600;
}

.description {
    color: var(--color-text);
    font-size: 1.1rem;
    line-height: 1.6;
    margin: 0 0 2rem 0;
    opacity: 0.9;
}

.contact-info {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    align-items: center;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--color-text);
    font-size: 1rem;
}

.contact-icon {
    font-size: 1.2rem;
}

.social-section {
    text-align: center;
}

.social-title {
    color: var(--color-heading);
    font-size: 1.2rem;
    margin: 0 0 1.5rem 0;
    font-weight: 600;
}

.social-links {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 1rem;
    max-width: 500px;
    margin: 0 auto;
}

.social-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem;
    background: var(--color-background-mute);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius);
    text-decoration: none;
    transition: all var(--transition-smooth);
    color: var(--color-text);
}

.social-link:hover {
    background: var(--color-primary);
    border-color: var(--color-primary);
    transform: translateY(-3px);
    color: var(--color-background);
}

.social-icon {
    width: 30px;
    height: 30px;
    transition: transform var(--transition-smooth);
}

.social-link:hover .social-icon {
    transform: scale(1.1);
}

.social-name {
    font-size: 0.9rem;
    font-weight: 500;
}

@media (max-width: 768px) {
    .hero-section {
        padding: 1rem;
        min-height: auto;
    }
    
    .presentation-card {
        padding: 2rem;
    }
    
    .social-links {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .contact-info {
        align-items: flex-start;
    }
}

@media (max-width: 480px) {
    .presentation-card {
        padding: 1.5rem;
    }
    
    .social-links {
        grid-template-columns: 1fr;
    }
    
    .card-content {
        gap: 2rem;
    }
}
</style>