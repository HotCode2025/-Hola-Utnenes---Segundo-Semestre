<script setup>
import { ref } from 'vue';
import iconEstudiante from '/src/assets/estudiante.png';

const titulo = 'Algunas de mis experiencias';
const fecha = '2025';

const experiencias = ref([
  { id: 1, src: iconEstudiante, parrafo: 'Trabajo de DJ en bares y boliches desde 2023' },
  { id: 2, src: iconEstudiante, parrafo: 'Diversas pasantías en laboratorios químicos' },
  { id: 3, src: iconEstudiante, parrafo: 'Diversas pasantías en trabajos mineros' },
  { id: 4, src: iconEstudiante, parrafo: "Estudiando y realizando proyectos para Técnico en Programación en la COHORTE 2025 - 'HOLA UTNENES' - UTN San Rafael." },
]);
</script>

<template>
  <div class="experiencia-container">
    <div class="card">
      <h3 class="titulo">{{ titulo }}</h3>
      <p class="fecha">{{ fecha }}</p>
      <ul class="listado">
        <li class="item" v-for="exp in experiencias" :key="exp.id">
          <div class="icono">
            <img :src="exp.src" alt="icono experiencia" />
          </div>
          <p class="texto">{{ exp.parrafo }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

.experiencia-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 3rem 1rem;
  background: linear-gradient(135deg, #1c1f26, #2e3545);
  min-height: 100vh;
  font-family: "Poppins", sans-serif;
}

.card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border-radius: 20px;
  padding: 2.5rem;
  width: min(800px, 90%);
  color: #f0f0f0;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.4);
}

.titulo {
  font-size: 1.8rem;
  font-weight: 700;
  color: #fff;
  text-align: center;
  margin-bottom: 0.3rem;
}

.fecha {
  text-align: center;
  font-size: 1rem;
  color: #aaa;
  margin-bottom: 1.5rem;
  letter-spacing: 1px;
}

.listado {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 14px;
  transition: transform 0.3s ease, background 0.3s ease, border-left 0.3s ease;
  border-left: 5px solid transparent;
}

.item:hover {
  transform: translateX(8px);
  background: rgba(255, 255, 255, 0.18);
  border-left-color: #41c49c;
}

.icono img {
  width: 45px;
  height: 45px;
  object-fit: cover;
  filter: brightness(1.05);
}

.texto {
  font-weight: 300;
  color: #e6e6e6;
  line-height: 1.5;
  margin: 0;
}

/* Responsive */
@media (max-width: 600px) {
  .card {
    padding: 1.8rem;
  }
  .titulo {
    font-size: 1.5rem;
  }
  .item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.8rem;
  }
}
</style>
