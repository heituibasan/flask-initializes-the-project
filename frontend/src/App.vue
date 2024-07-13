<template>
	<a-spin :spinning="loading" tip="加载中...">
		<scroll-wrapper>
			<router-view/>
		</scroll-wrapper>
	</a-spin>
</template>

<script setup lang="ts">
import {ref, onMounted} from "vue";
import ScrollWrapper from './components/public/ScrollWrapper.vue';

const loading = ref(true);

onMounted(() => {
	loading.value = false;  // 组件挂载完成停止刷新
});
</script>