<script setup>
import { ref } from 'vue'

const estudios = ref([
  { institucion: 'Instituto Jorge Coll', titulo: 'Profesora de Educación Física', periodo: '2015-2018' },
  { institucion: 'UTN', titulo: 'Técnica en Programación', periodo: '2025 - Actualidad' }
])
</script>

<template>
  <section id="educacion" class="educacion">
    <h2>Educación</h2>
    <div class="cards">
      <div v-for="e in estudios" :key="e.titulo" class="card">
        <h3>{{ e.titulo }}</h3>
        <p>{{ e.institucion }}</p>
        <span>{{ e.periodo }}</span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.educacion {
  background: linear-gradient(135deg, #e0baff, #c18bff, #a355ff);
  padding: 80px 50px;
  border-radius: 25px;
  width: 90%;
  margin: 40px auto;
  text-align: center;
  color: black;
}

h2 {
  font-size: 2.8rem;
  margin-bottom: 30px;
  font-weight: bold;
  color: black; 
}

.cards {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  background: #d8b4ff; 
  color: black; 
  border-radius: 55px;
  padding: 55px;
  width: 300px;
  max-width: 100%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.4);
}

.card h3 {
  font-size: 2.2rem;
  margin-bottom: 10px;
  color: black;
}

.card p,
.card span {
  font-size: 1.9rem;
  color: black;
}


@media (max-width: 1024px) {
  .card {
    padding: 45px;
  }
  .card h3 {
    font-size: 2rem;
  }
  .card p,
  .card span {
    font-size: 1.7rem;
  }
}

@media (max-width: 768px) {
  .cards {
    flex-direction: column;
    align-items: center;
  }
  .card {
    width: 90%;
    padding: 35px;
  }
  .card h3 {
    font-size: 1.8rem;
  }
  .card p,
  .card span {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .educacion {
    padding: 40px 15px;
  }
  h2 {
    font-size: 2.2rem;
    margin-bottom: 20px;
  }
  .card h3 {
    font-size: 1.6rem;
  }
  .card p,
  .card span {
    font-size: 1.3rem;
  }
}
</style>
