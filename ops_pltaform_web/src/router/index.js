import {createRouter, createWebHistory} from "vue-router";
import Layout from '../Layout/index.vue'

const routes = [

    {
        path: '/login',
        name: 'login',
        component: () => import ('../views/login.vue'),
    },

    {
        path: '/uric',
        name: 'uric',
        alias: "/",
        component: Layout,
        meta: {
            title: '运维平台',
            authenticate: true,
        },
        children: [
            {
                path: 'hosts',
                name: 'Hosts',
                component: () => import('../views/hosts.vue')
            },
                        {
                path: 'ShowCenter',
                name: 'ShowCenter',
                component: () => import('../views/ShowCenter.vue')
            }
        ]
    },

]


const router = createRouter({
        history: createWebHistory(),   //路由1显示模式
        routes
    }
);

router.beforeEach((to, from, next) => {

    let token = localStorage.token || sessionStorage.token
    if (to.meta.authenticate && !token) {
        console.log(" back to login")
        next({name: 'login'})
    } else {
        console.log("go to next")
        next()
    }

})
export default router;
