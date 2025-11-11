<script setup>
// IMPORTACIONES
import linkedin from '/src/assets/linkedin.png';
import instagram from '/src/assets/instagram.png';
import github from '/src/assets/github.png';

const nombreJoaco = 'Joaquin Ybañez';
const descripcionJoaco = 'Técnico Universitario en Programación - UTN / Técnico Industrial y Minero';
const residenciaJoaco = 'Mendoza, Argentina';
const presentacionJoaco = 'Apasionado por el deporte, la tecnología, la música y las buenas personas.';
const telefonoJoaco = '+54 2604 600 903';

const contactItems = [
  { icon: '📍', text: residenciaJoaco },
  { icon: '📞', text: telefonoJoaco }
];

const redesSocialesJoaco = [
  { id: 1, nombre: 'LinkedIn', src: linkedin, url: 'https://www.linkedin.com' },
  { id: 2, nombre: 'Instagram', src: instagram, url: 'https://www.instagram.com' },
  { id: 3, nombre: 'Github', src: github, url: 'https://github.com' }
];
</script>

<template>
  <section class="hero-section">
    <div class="card">
      <div class="card-left">
        <h1 class="main-title">{{ nombreJoaco }}</h1>
        <h2 class="role">{{ descripcionJoaco }}</h2>
        <p class="description">{{ presentacionJoaco }}</p>

        <div class="contact-info">
          <div v-for="(contact, index) in contactItems" :key="index" class="contact-item">
            <span class="contact-icon">{{ contact.icon }}</span>
            <span>{{ contact.text }}</span>
          </div>
        </div>
      </div>

      <div class="card-right">
        <h3 class="social-title">Conectemos</h3>
        <div class="social-links">
          <a
            v-for="red in redesSocialesJoaco"
            :key="red.id"
            :href="red.url"
            class="social-link"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img class="social-icon" :src="red.src" :alt="red.nombre" />
            <span class="social-name">{{ red.nombre }}</span>
          </a>
        </div>
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
  padding: 3rem;
  background: linear-gradient(135deg, #f5f3ff, #eef2ff);
}

.card {
  display: grid;
  grid-template-columns: 1fr 0.8fr;
  background: #ffffffcc;
  backdrop-filter: blur(10px);
  border-radius: 20px;
  box-shadow: 0 15px 40px rgba(99, 102, 241, 0.2);
  overflow: hidden;
  max-width: 1000px;
  width: 100%;
  transition: all 0.3s ease;
  border: 1px solid rgba(147, 197, 253, 0.3);
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 25px 60px rgba(147, 197, 253, 0.25);
}

.card-left {
  padding: 3rem;
  background: linear-gradient(160deg, #ede9fe 0%, #dbeafe 100%);
}

.card-right {
  padding: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: linear-gradient(135deg, #a78bfa15, #60a5fa15);
}

/* ✅ Corregimos el error usando :deep() */
:deep(.main-title) {
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 800;
  background: linear-gradient(90deg, #a78bfa, #60a5fa);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  margin-bottom: 1rem;
}

.role {
  color: #4f46e5;
  font-weight: 600;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.description {
  color: #444;
  font-size: 1.05rem;
  line-height: 1.7;
  margin-bottom: 2rem;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #374151;
  font-size: 1rem;
}

.contact-icon {
  font-size: 1.3rem;
}

.social-title {
  color: #4f46e5;
  font-size: 1.3rem;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 600;
}

.social-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.9rem 1.2rem;
  border-radius: 10px;
  text-decoration: none;
  color: #374151;
  font-weight: 500;
  background: #f9fafb;
  border: 1px solid rgba(147, 197, 253, 0.3);
  transition: all 0.3s ease;
}

.social-link:hover {
  background: linear-gradient(90deg, #a78bfa, #60a5fa);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(147, 197, 253, 0.25);
}

.social-icon {
  width: 28px;
  height: 28px;
  transition: transform 0.3s ease;
}

.social-link:hover .social-icon {
  transform: scale(1.1);
}

.social-name {
  font-size: 1rem;
}

@media (max-width: 900px) {
  .card {
    grid-template-columns: 1fr;
  }
  .card-left, .card-right {
    padding: 2rem;
  }
  .social-links {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>


