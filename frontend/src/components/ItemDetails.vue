<template>
  <div v-if="item">
    <h1>{{ item.name }}</h1>
    <img :src="item.image" alt="Image of item" />
    <p>{{ item.description }}</p>
    <h2>Stores</h2>
    <ul>
      <li v-for="store in item.stores" :key="store.name">
        {{ store.name }}: {{ store.price }}
      </li>
    </ul>
  </div>
  <div v-else>
    <p>Loading item details...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      item: null
    };
  },
  created() {
    const itemId = this.$route.params.id;
    axios
      .get(`/item/${itemId}`)
      .then((response) => {
        this.item = response.data;
      })
      .catch((error) => {
        console.error("Error loading item details:", error);
      });
  }
};
</script>

<style scoped>
img {
  width: 150px;
  height: 150px;
}
</style>
