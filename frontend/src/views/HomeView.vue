<template>
	<a-upload-dragger v-model:fileList="fileList" name="file" :multiple="true" :action="putUrl" @change="handleChange"
	                  @drop="handleDrop">
		<p class="ant-upload-drag-icon">
			<inbox-outlined></inbox-outlined>
		</p>
		<p class="ant-upload-text">点击或拖入上传文件</p>
		<p class="ant-upload-hint">
			支持单次或批量上传。严禁上传公司数据或其他标注栏文件
		</p>
	</a-upload-dragger>
</template>
<script lang="ts" setup>
import {ref} from 'vue';
import {InboxOutlined} from '@ant-design/icons-vue';
import {message} from 'ant-design-vue';
import type {UploadChangeParam} from 'ant-design-vue';
import {baseUrl} from "@/utils/config";
// 变量
const fileList = ref([]);
const putUrl = baseUrl + "/file/upload"		// 文件上传url
// 上传文件
const handleChange = (info: UploadChangeParam) => {
	const status = info.file.status;
	if (status !== 'uploading') {

	}
	if (status === 'done') {
		const response = info.file.response;
		if (response.status === "error") {
			message.error(response.message);
			return;
		}
		message.success(`${info.file.name} 文件上传成功`);
	}
};

function handleDrop(e: DragEvent) {
	console.log(e);
}
</script>