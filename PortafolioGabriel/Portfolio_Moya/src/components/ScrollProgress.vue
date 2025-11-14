<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const progress = ref(0);

const updateProgress = () => {
  const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

  const totalScrollable = scrollHeight - clientHeight;
  const value = totalScrollable > 0 ? (scrollTop / totalScrollable) * 100 : 0;

  progress.value = Math.min(Math.max(value, 0), 100); // entre 0 y 100
};

onMounted(() => {
  window.addEventListener("scroll", updateProgress);
  updateProgress();
});

onUnmounted(() => {
  window.removeEventListener("scroll", updateProgress);
});
</script>

<template>
  <div class="scroll-bar">
    <div class="scroll-bar__inner" :style="{ width: progress + '%' }"></div>
  </div>
</template>

<style scoped>
.scroll-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.08);
  z-index: 9999;
}

.scroll-bar__inner {
  height: 100%;
  width: 0;
  background: linear-gradient(90deg, #ff8000, #ffc857);
  transition: width 0.1s linear;
}
</style>
