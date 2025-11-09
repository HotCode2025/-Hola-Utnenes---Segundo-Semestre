<script setup>
import { ref } from 'vue';
const misProyectos = ref([
  { id: 1, titulo: 'Aplicación de Inventario (2025)', descripcion: 'Proceso de inventario, creado en Java junto a mi grupo de trabajo HolaUTNenes..', projectoLink: '#', githubLink: 'https://github.com/HotCode2025/-Hola-Utnenes---Segundo-Semestre' },
  { id: 2, titulo: 'Aplicación "Dividir la Cuenta" (2022)', descripcion: 'Aplicación móvil creada en Swift, que divide los gastos totales entre las personas participantes.', projectoLink: '#', githubLink: '#' },
  { id: 3, titulo: 'Cotizador de seguros (2021)', descripcion: 'Web realizada con Html, CSS y Javascript, conectada a una API para cotizar seguros.', projectoLink: 'https://zealous-nightingale-3c14e3.netlify.app/', githubLink: 'https://github.com/fernandohds/Cotizador-de-seguros' },
]);
</script>

<template>
  <div class="galeria">
    <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a :href="proyecto.projectoLink" class="btn-ver-mas" target="_blank">Ver Proyecto</a>
          <a :href="proyecto.githubLink" class="github-link" target="_blank">Ver Código</a>
        </div>
      </div>
    </li>
  </div>
</template>

<style scoped>
.galeria {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  background-color: var(--color-bg-dark);
}
.proyecto {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-left: 5px solid var(--color-accent);
  border-radius: 10px;
  overflow: hidden;
  width: 280px;
  box-shadow: 0 0 20px rgba(255, 213, 79, 0.15);
  transition: 0.3s;
}
.proyecto:hover {
  transform: translateY(-6px);
  box-shadow: 0 0 25px rgba(255, 213, 79, 0.3);
}
.proyecto-info {
  padding: 1rem;
  text-align: center;
}
.proyecto-info h3 { color: var(--color-accent); font-size: 1.3rem; }
.proyecto-info p { color: var(--color-text-light); }
.btn-ver-mas {
  background-color: var(--color-accent);
  color: #000;
  padding: 0.5rem;
  border-radius: 5px;
  display: inline-block;
  margin-top: 1rem;
}
.btn-ver-mas:hover { background-color: var(--color-accent-hover); }
.github-link { color: var(--color-text-light); font-size: 0.9em; }
.github-link:hover { color: var(--color-accent); }
</style>
