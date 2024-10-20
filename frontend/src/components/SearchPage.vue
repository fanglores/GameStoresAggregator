<template>
  <div class="search-page">
    <h1>Search Items</h1>
    <input
      type="text"
      v-model="query"
      @keypress.enter="searchItems"
      placeholder="Type to search..."
    />
    <ul v-if="results.length > 0">
      <li v-for="(item, index) in results" :key="index">
        <router-link :to="'/item/' + index">{{ item.game_name }}</router-link>
        <p>Store: {{ item.store_name }} - Price: {{ item.price }}</p>
      </li>
    </ul>
    <p v-else>No results found</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchPage',
  data() {
    return {
      query: '',
      results: []
    };
  },
  methods: {
    searchItems() {
      if (this.query.trim() === '') {
        alert('Please enter a search term');
        return;
      }

      axios
        .get(`/search?query=${encodeURIComponent(this.query)}`)
        .then((response) => {
          if (response.data.success) {
            this.results = response.data.result;
          } else {
            this.results = [];
          }
        })
        .catch((error) => {
          console.error("There was an error!", error);
        });
    }
  }
};
</script>

<style scoped>
.search-page {
  text-align: center;
}
input {
  padding: 10px;
  width: 300px;
  font-size: 16px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 10px 0;
}
</style>
