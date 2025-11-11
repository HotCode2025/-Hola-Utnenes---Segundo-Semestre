<script setup>
import { ref } from 'vue'

const experiencias = ref([
  { 
    puesto: 'Administrativa', 
    tareas: 'Manejo de tesorería y sistemas internos.', 
    periodo: '2019 - Actualidad' 
  }
])
</script>

<template>
  <section id="experiencia" class="experiencia">
    <h2>Experiencia</h2>
    <div class="cards">
      <div v-for="exp in experiencias" :key="exp.puesto" class="card">
        <h3>{{ exp.puesto }}</h3>
        <p>{{ exp.tareas }}</p>
        <span>{{ exp.periodo }}</span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.experiencia {
  background: linear-gradient(135deg, #e0baff, #c18bff, #a355ff);
  padding: 60px 30px;
  border-radius: 5%;
  width: 90%;
  margin: 40px auto;
  text-align: center;
  color: black;
}

h2 {
  font-size: 2.9rem;
  margin-bottom: 30px;
  font-weight: bold;
  color: black;
}

.cards {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 25px;
}

.card {
  background: #d8b4ff; 
  color: black;
  border-radius: 25px;
  padding: 30px;
  width: 800px; /* ancho para escritorio */
  max-width: 100%; /* evita que se salga en pantallas pequeñas */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: left;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.card h3 {
  font-size: 2.7rem;
  margin-bottom: 12px;
  font-weight: 600;
}

.card p {
  font-size: 2.5rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

.card span {
  font-size: 1.7rem;
  font-weight: bold;
  color: #333;
}

/* Media queries para pantallas más pequeñas */
@media (max-width: 1024px) {
  .card {
    padding: 25px;
  }
  .card h3 {
    font-size: 2.3rem;
  }
  .card p {
    font-size: 2rem;
  }
  .card span {
    font-size: 1.5rem;
  }
}

@media (max-width: 768px) {
  .cards {
    flex-direction: column;
    align-items: center;
  }
  .card {
    width: 90%;
    padding: 20px;
  }
  .card h3 {
    font-size: 2rem;
  }
  .card p {
    font-size: 1.8rem;
  }
  .card span {
    font-size: 1.3rem;
  }
}

@media (max-width: 480px) {
  .experiencia {
    padding: 40px 15px;
  }
  h2 {
    font-size: 2.2rem;
    margin-bottom: 20px;
  }
  .card h3 {
    font-size: 1.8rem;
  }
  .card p {
    font-size: 1.6rem;
  }
  .card span {
    font-size: 1.2rem;
  }
}
</style>
