<script setup>
import { ref } from 'vue';
import iconSewing from '/src/assets/sewing-machine-svgrepo-com.svg';
import iconEstudiante from '/src/assets/student-person-svgrepo-com.svg';


const titulo = 'Estudiantes Para Desarrolladores Full Stack';
const fecha = 'Enero 2025 - Enero 2027';


const experiencia = ref([
    { id: 1, src: iconSewing, parrafo: 'Modista Independiente/Taller Propio (2020 - Actualidad): Confección a medida de prendas de alta costura, incluyendo vestidos de fiesta y trajes formales. Gestión de clientes y pedidos personalizados' }, 
    { id: 2, src: iconEstudiante, parrafo: 'Estudiando y haciendo proyectos para tectnico en programacion en COHORTE 2025 - ("HOLA UTNENES") - UTN SAN RAFAEL '},
]);
</script>


<template>
  <div>
    <div class="card">
        <h3 class="titulo"> {{ titulo }}</h3>
        <p class="fecha"> {{ fecha }} </p>
        <ul class="listado">
            <li class='item' v-for='exp in experiencia' :key="exp.id">
                <img :src='exp.src' alt="" width="45rem" :alt="exp.parrafo">
                <p>{{ exp.parrafo }}</p>
            </li>
        </ul>
    </div>
  </div>
</template>

<style scoped>
.card {
  background: linear-gradient(135deg, #fff0f5, #f0fff0); /* rosa claro a lima suave */
  border: 2px solid #ff69b4;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(255, 105, 180, 0.2);
  color: #333;
}

.titulo {
  color: #ff1493;
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  text-align: center;
  text-shadow: 1px 1px 0 #fff;
}

.fecha {
  font-size: 1rem;
  color: #32cd32;
  text-align: center;
  margin-bottom: 1.5rem;
  font-weight: 500;
}

.listado {
  list-style: none;
  padding: 0;
  margin: 0;
}

.item {
  background-color: #fafffa;
  border-left: 6px solid #32cd32;
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: transform 0.2s ease, background-color 0.3s ease;
}

.item:hover {
  background-color: #ffe4ec;
  transform: scale(1.02);
}

.item img {
  width: 45px;
  height: 45px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #ff69b4;
  background-color: #fff;
}

.item p {
  margin: 0;
  font-weight: 500;
  color: #444;
}
</style>