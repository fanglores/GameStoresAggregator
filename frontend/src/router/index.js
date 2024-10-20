import { createRouter, createWebHistory } from 'vue-router';
import SearchPage from '../components/SearchPage.vue';
import ItemDetails from '../components/ItemDetails.vue';

const routes = [
  {
    path: '/',
    name: 'SearchPage',
    component: SearchPage
  },
  {
    path: '/item/:id',
    name: 'ItemDetails',
    component: ItemDetails
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
