<template>
	<div :style="backgroundStyle">
		<!-- 你可以在这里添加其他内容 -->
	</div>
</template>

<script lang="ts" setup>
import {ref, onMounted} from 'vue';

// 响应式变量用于存储背景图片的 URL
const backgroundUrl = ref('');


// 动态计算背景样式
const backgroundStyle = computed(() => ({
	width: '100vw',
	height: '100vh',
	backgroundImage: `url(${backgroundUrl.value})`,
	backgroundSize: 'cover',
	backgroundPosition: 'center',
	backgroundRepeat: 'no-repeat',
}));
</script>

<style scoped>
/* 你可以在这里添加其他样式 */
</style>