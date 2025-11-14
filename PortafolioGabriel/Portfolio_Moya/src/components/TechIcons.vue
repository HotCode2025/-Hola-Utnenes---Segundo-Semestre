<script setup>
import arduino from "../assets/icons/arduino.svg";
import bambulab from "../assets/icons/bambulab.svg";
import cplusplus from "../assets/icons/cplusplus.svg";
import esphome from "../assets/icons/esphome.svg";
import github from "../assets/icons/github.svg";
import googleappsscript from "../assets/icons/googleappsscript.svg";
import html from "../assets/icons/html.svg";
import javascript from "../assets/icons/javascript.svg";
import python from "../assets/icons/python.svg";
import wordpress from "../assets/icons/wordpress.svg";

const techs = [
  { name: "Arduino", icon: arduino },
  { name: "Bambu Lab", icon: bambulab },
  { name: "C++", icon: cplusplus },
  { name: "ESPHome", icon: esphome },
  { name: "GitHub", icon: github },
  { name: "Google Apps Script", icon: googleappsscript },
  { name: "HTML", icon: html },
  { name: "JavaScript", icon: javascript },
  { name: "Python", icon: python },
  { name: "WordPress", icon: wordpress },
];
</script>

<template>
  <section class="tech-icons">
    <h3>Stack tecnológico destacado</h3>

    <div class="icons-grid">
      <div v-for="tech in techs" :key="tech.name" class="icon-item">
        <img :src="tech.icon" :alt="tech.name" />
        <span>{{ tech.name }}</span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.tech-icons {
  margin-top: 24px;
}

.tech-icons h3 {
  color: orange;
  margin-bottom: 12px;
  font-size: 1.1rem;
}

.icons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
  gap: 18px;
}

.icon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: #ddd;
}

/* Tus SVGs se pueden colorear con filter */
.icon-item img {
  width: 42px;
  height: 42px;
  filter: invert(80%) sepia(60%) saturate(700%) hue-rotate(5deg);
  transition: transform 0.2s ease, filter 0.2s ease;
}

.icon-item img:hover {
  transform: scale(1.15);
  filter: invert(100%) sepia(100%) saturate(2000%) hue-rotate(25deg);
}
</style>
