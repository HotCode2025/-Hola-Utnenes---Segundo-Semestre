<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';
const title = 'Fernando Figueroa'
const descripcion = 'Técnico Universitario en Programación - UTN'
const residencia = 'Mar del Plata, Buenos Aires, Argentina'
const presentacion = 'Hola, Bienvenido a mi portafolio. Soy un desarrollador web con experiencia en el desarrollo de aplicaciones web y móviles.'
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/in/fernando-figueroa-hds/' },
  { id: 2, name: 'Instagram', src: instagram, url: 'https://instagram.com' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/fernandohds' },
]
const telefono = '+54 9 2474492984'
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url" target="_blank">
            <img class="icon-redsocial" :src="red.src" width="35" :alt="red.name">
          </a>
        </li>
      </ul>
      <h3>☎ {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
.card {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 0 15px rgba(255, 213, 79, 0.1);
}
h1 { color: var(--color-accent); font-size: 2.2rem; }
p { font-size: 1.2rem; margin: 1rem 0; }
.icon-redsocial {
  border-radius: 50%;
  background-color: var(--color-accent);
  padding: 6px;
  margin: 5px;
  transition: 0.3s;
}
.icon-redsocial:hover {
  transform: scale(1.2);
  background-color: var(--color-accent-hover);
}
h3, h4 { color: var(--color-text-light); font-weight: 500; }
</style>
