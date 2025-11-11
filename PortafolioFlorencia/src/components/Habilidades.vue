<script setup>
import { ref } from 'vue'

import imgJava from '@/assets/img/java.png'
import imgPython from '@/assets/img/python.png'
import imgJS from '@/assets/img/javascript.png'
import imgVue from '@/assets/img/vue.png'
import imgGitHub from '@/assets/img/github.png'

const habilidades = ref([
  { nombre: 'Java', icono: imgJava },
  { nombre: 'Python', icono: imgPython },
  { nombre: 'JavaScript', icono: imgJS },
  { nombre: 'Vue.js', icono: imgVue },
  { nombre: 'GitHub', icono: imgGitHub }
])
</script>

<template>
  <section id="habilidades" class="habilidades">
    <h2>Habilidades</h2>
    <ul>
      <li v-for="(h, i) in habilidades" :key="i">
        <img :src="h.icono" :alt="h.nombre" class="icono" />
        <span>{{ h.nombre }}</span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.habilidades {
  background: linear-gradient(135deg, #e0baff, #c18bff, #a355ff);
  padding: 60px 30px;
  border-radius: 25px;
  width: 90%;
  margin: 40px auto;
  text-align: center;
  color: black;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
}

ul {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 25px;
  list-style: none;
  padding: 0;
}

li {
  background-color: #d8b4ff;
  color: black;
  padding: 20px 30px;
  border-radius: 30px;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

li:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.icono {
  width: 100px;
  height: 70px;
  object-fit: contain;
}


@media (max-width: 1024px) {
  li {
    padding: 18px 25px;
  }
  .icono {
    width: 80px;
    height: 60px;
  }
  h2 {
    font-size: 2.2rem;
  }
}

@media (max-width: 768px) {
  ul {
    flex-direction: column;
    align-items: center;
  }
  li {
    width: 90%;
    justify-content: flex-start;
    padding: 15px 20px;
    gap: 15px;
  }
  .icono {
    width: 70px;
    height: 50px;
  }
  h2 {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  li {
    padding: 12px 15px;
    gap: 10px;
  }
  .icono {
    width: 60px;
    height: 45px;
  }
  h2 {
    font-size: 1.8rem;
  }
}
</style>
