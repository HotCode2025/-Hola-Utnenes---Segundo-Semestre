<script setup>
const title ="Fernanda Diaz";
const descripcion="Tecnico Universitario en Programacion - UTN";
const residencia="Tupungato, Mendoza, Argentina";
const presentacion="Hola, bienvenido/a a mi portafolio de proyectos. Soy una estudiante de desarrollo de aplicaciones web y moviles";
import instagram from '/src/assets/icons8-instagram-50.png'
import linkedin from '/src/assets/icons8-linkedin-50.png'
import cv from '/src/assets/icons8-analizar-el-curriculum-vitae-80.png'
import github from '/src/assets/github-svgrepo-com.svg'

const redesSociales= [
  { id: 1, name: 'linkedin', src: linkedin, url: '' },
  { id: 2, name: 'instagram', src: instagram, url: 'https://www.instagram.com/ferdia.z/' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/ferdiaz9' },
  { id: 4, name: 'curriculum', src: cv, url: 'file:///D:/Mis%20Cosas/Descargas/DOC-20250821-WA0021.%20(2).pdf' },
];
const telefono = '2622-374740';
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
        <img 
          :src="red.src" 
          class="icon-redsocial" 
          width="35rem" 
          :alt="red.name" 
        /> 
      </a>
    </li>
  </ul>
      
      <h3> Mi telefono personal:{{telefono}}</h3>
      <h4>{{residencia}}</h4>
     </div>
  </section>
</template>

<style scoped>
.datos-personales {
  display: flex;
  justify-content: center;
  padding: 2rem;
  background-color: #fff8f0; /* fondo blanco cálido */
}

.card {
  background: linear-gradient(135deg, #ffe4e1, #fffacd); /* rosa claro a amarillo claro */
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  max-width: 600px;
  width: 100%;
  text-align: center;
  color: #4a4a4a;
}

.card h1 {
  font-size: 2rem;
  color: #ff69b4; /* rosa fuerte */
  margin-bottom: 0.5rem;
}

.card h2 {
  font-size: 1.5rem;
  color: #ffa500; /* naranja suave */
  margin-bottom: 1rem;
}

.card p {
  font-size: 1rem;
  margin-bottom: 1.5rem;
  color: #555;
}

.container-lista {
  display: flex;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin-bottom: 1.5rem;
}

.icon-redsocial {
  transition: transform 0.3s ease;
  border-radius: 50%;
  background-color: #fff;
  padding: 0.3rem;
}

.icon-redsocial:hover {
  transform: scale(1.2);
  background-color: #ffebcd; /* beige claro */
}

.card h3 {
  font-size: 1.2rem;
  color: #ff1493; /* rosa intenso */
  margin-bottom: 0.5rem;
}

.card h4 {
  font-size: 1rem;
  color: #daa520; /* dorado suave */
}
</style>