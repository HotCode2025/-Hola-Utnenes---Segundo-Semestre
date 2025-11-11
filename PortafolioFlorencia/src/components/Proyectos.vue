<script setup>
import { ref } from 'vue'

import imgPortafolio from '@/assets/img/portafolio_html.png'
import imgTareas from '@/assets/img/tareas_pseint.png'

const proyectos = ref([
  { 
    titulo: 'Mi portafolio', 
    descripcion: 'Portafolio personal en Vue.js con diseño responsive.',
    imagen: imgPortafolio, 
    enlace: '#' 
  },
  { 
    titulo: 'App de tareas', 
    descripcion: 'Gestor de tareas realizado con PSeInt.',
    imagen: imgTareas, 
    enlace: '#' 
  }
])
</script>

<template>
  <section id="proyectos" class="proyectos">
    <h2>Proyectos</h2>
    <div class="cards">
      <div v-for="p in proyectos" :key="p.titulo" class="card">
        <img :src="p.imagen" alt="Imagen del proyecto" class="img-proyecto" />
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.descripcion }}</p>
        <a :href="p.enlace" target="_blank">Ver proyecto</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.proyectos {
  background: linear-gradient(135deg, #e0baff, #c18bff, #a355ff);
  padding: 60px 30px;
  border-radius: 25px;
  width: 90%;
  margin: 50px auto;
  text-align: center;
  color: black;
}

h2 {
  font-size: 2.8rem;
  margin-bottom: 30px;
  font-weight: bold;
}

.cards {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 25px;
}

.card {
  background: #ffb4f6;
  color: black;
  border-radius: 35px;
  padding: 40px;
  width: 280px;
  max-width: 100%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.img-proyecto {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 15px;
}

.card h3 {
  font-size: 1.9rem;
  margin-bottom: 10px;
}

.card p {
  font-size: 1.5rem;
  margin-bottom: 15px;
}

.card a {
  display: inline-block;
  background: #a355ff;
  color: white;
  font-weight: bold;
  text-decoration: none;
  padding: 8px 15px;
  border-radius: 20px;
  transition: background 0.3s ease;
}

.card a:hover {
  background: #7f00ff;
}

@media (max-width: 1024px) {
  .card {
    padding: 35px;
  }
  .card h3 {
    font-size: 1.7rem;
  }
  .card p {
    font-size: 1.4rem;
  }
  .card a {
    padding: 7px 14px;
  }
}

@media (max-width: 768px) {
  .cards {
    flex-direction: column;
    align-items: center;
  }
  .card {
    width: 90%;
    padding: 30px;
  }
  .card h3 {
    font-size: 1.6rem;
  }
  .card p {
    font-size: 1.3rem;
  }
  .card a {
    padding: 6px 12px;
  }
}

@media (max-width: 480px) {
  .proyectos {
    padding: 40px 15px;
  }
  h2 {
    font-size: 2.2rem;
    margin-bottom: 20px;
  }
  .card h3 {
    font-size: 1.4rem;
  }
  .card p {
    font-size: 1.2rem;
  }
  .card a {
    padding: 5px 10px;
    font-size: 1rem;
  }
}
</style>
