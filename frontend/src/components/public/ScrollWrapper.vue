<template>
	<div class="scroll-container">
		<div class="scroll-content">
			<slot></slot>
		</div>
	</div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.scroll-container {
	max-height: 100vh;
	/* 你可以根据需要调整 */
	overflow-y: auto;
}

.scroll-container::-webkit-scrollbar {
	width: 8px;
}

.scroll-container::-webkit-scrollbar-thumb {
	background: #9e9d9d;
	border-radius: 4px;
}

.scroll-container::-webkit-scrollbar-thumb:hover {
	background: #868686;
}
</style>