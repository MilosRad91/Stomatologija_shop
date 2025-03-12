import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ShopKupacView from '../views/ShopKupacView.vue';
import ShopProdavacView from '../views/ShopProdavacView.vue';
import ShopAdminView from '../views/ShopAdminView.vue';
import ProfileView from '@/views/ProfileView.vue';
import CartView from '@/views/CartView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from, next) => {
        const get_korisnik = sessionStorage.getItem('korisnik');
        const korisnik = JSON.parse(get_korisnik)
        if(korisnik){
          next({ name: 'error_page' });
        }
        if (korisnik == null) {
          next(); // Dozvoli pristup
        } 
        else {
          next({ name: 'error_page' }); // Preusmeri na drugu stranicu, ako nije kupac
        }
      }
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
    },
    {
      path: '/error',
      name: 'error_page',
      component: () => import('../views/ErrorPageView.vue'),
    },
    {
      path: '/shop/kupac',
      name: 'shop-kupac',
      component: ShopKupacView,
      beforeEnter: (to, from, next) => {
        const get_korisnik = sessionStorage.getItem('korisnik');
        const korisnik = JSON.parse(get_korisnik)
        if(korisnik == null){
          next({ name: 'error_page' });
        }
        if (korisnik.vrsta_korisnika === 'kupac') {
          next(); // Dozvoli pristup
        } 
        else {
          next({ name: 'error_page' }); // Preusmeri na drugu stranicu, ako nije kupac
        }
      }
    },
    {
      path: '/shop/prodavac',
      name: 'shop-prodavac',
      component: ShopProdavacView,
      beforeEnter: (to, from, next) => {
        const get_korisnik = sessionStorage.getItem('korisnik');
        const korisnik = JSON.parse(get_korisnik)
        if(korisnik == null){
          next({ name: 'error_page' });
        }
        if (korisnik.vrsta_korisnika === 'prodavac') {
          next(); // Dozvoli pristup
        } 
        else {
          next({ name: 'error_page' }); // Preusmeri na drugu stranicu, ako nije kupac
        }
      }
    },
    {
      path: '/shop/admin',
      name: 'shop-admin',
      component: ShopAdminView,
      beforeEnter: (to, from, next) => {
        const get_korisnik = sessionStorage.getItem('korisnik');
        const korisnik = JSON.parse(get_korisnik)
        if(korisnik == null){
          next({ name: 'error_page' });
        }
        if (korisnik.vrsta_korisnika === 'admin') {
          next(); // Dozvoli pristup
        } 
        else {
          next({ name: 'error_page' }); // Preusmeri na drugu stranicu, ako nije kupac
        }
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/cart-view',
      name: 'cart-view',
      component: CartView
    }
  ],
})

export default router
