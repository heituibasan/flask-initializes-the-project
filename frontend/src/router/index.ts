import {createRouter, createWebHistory} from 'vue-router'
import {checkToken} from "@/api/user"
import {message} from 'ant-design-vue';
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,

        },
        {
            path: '/admin',
            name: 'Admin',
            children: [
                {
                    path: 'login',
                    name: 'UserLogin',
                    component: () => import('@/views/admin/login.vue'),
                },
                {
                    path: 'register',
                    name: 'UserRegister',
                    component: () => import('@/views/admin/register.vue'),
                },
                {
                    path: 'forget',
                    name: 'UserForget',
                    component: () => import('@/views/admin/forget.vue'),
                },
                {
                    path: 'reset',
                    name: 'UserReset',
                    component: () => import('@/views/admin/reset.vue'),
                },
            ]
        }
    ]
})


// 获取加载动画的 DOM 元素
const loadingElement = document.getElementById("app-cockpit-loading");

// 添加全局导航守卫
router.beforeEach(async (to, from, next) => {
    // 在请求发送之前显示加载动画
    if (loadingElement) {
        loadingElement.style.display = "block";
    }
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const token = localStorage.getItem('token');

    // 检查如果访问/back,则跳转到/back/console
    // if (to.path === '/back'){
    //     next('/back/console');
    // }

    if (requiresAuth) {
        if (!token) {
            // 如果没有 token 并且访问的路由需要登录，跳转到登录页
            message.error("用户未登录", 1);
            next({
                path: '/admin/login',
                query: {redirect: to.fullPath},
            });
        } else {
            try {
                // 检查 token 的有效性
                const ResponseResult = await checkToken(token);
                if (ResponseResult.data.status === "error") { // 如果已经过期
                    message.error("登录已过期", 1);
                    next({
                        path: '/admin/login',
                        query: {redirect: to.fullPath},
                    });

                } else {
                    next();

                }
                // 修改为检查本地token内的信息是否过期，不需要发起请求
                // next();
            } catch (error) {
                // 如果 token 无效，移除 token 并跳转到登录页
                localStorage.removeItem('token');
                localStorage.removeItem('user');
                message.error("登录已过期", 1);
                next({
                    path: '/admin/login',
                    query: {redirect: to.fullPath},
                });
            }
        }
    } else {
        // 检查是否已登录且访问的是登录或注册页面
        if ((to.path === '/admin/login' || to.path === '/admin/register') && token) {
            try {
                const ResponseResult = await checkToken(token);
                if (ResponseResult.data.status !== "error") {
                    // 如果已登录，重定向到 /back/index
                    next('/back/console');
                } else {
                    next();
                }
            } catch (error) {
                next();
            }
        } else {
            next(); // 如果不需要登录，允许进入路由
        }
    }


});
// 隐藏加载动画
if (loadingElement) {
    loadingElement.style.display = "none";
}
export default router
