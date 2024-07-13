<template>
	<a-card :style="backgroundStyle">
		<a-flex justify="center" style="margin-top: 20vh">
			<a-space direction="vertical" size="middle" style="width: 300px">
				<a-typography-title style="padding-left: 5px"
				><strong>Register</strong></a-typography-title
				>
				<a-input v-model:value="userInfo.email" type="email" placeholder="邮箱"/>
				<a-input-password
					v-model:value="userInfo.password"
					placeholder="密码"
				/>
				<a-input-password
					v-model:value="userInfo.confirm"
					placeholder="确认密码"
				/>
				<span>
          <a-typography-link href="/user/login" style="float: right"
          >返回登录</a-typography-link
          >
        </span>
				<a-button type="primary" @click="handleRegister" style="width: 300px"
				>注册
				</a-button
				>
			</a-space>
		</a-flex>
	</a-card>
</template>
<script lang="ts" setup>
import {ref, reactive, computed} from "vue";
import {message} from "ant-design-vue";
import {isValidEmail} from "@/utils/tools";
import {register} from "@/api/admin";
import {useRouter} from "vue-router";
import {checkDevice} from "@/utils/tools";

const router = useRouter();
const userInfo: object = reactive({
	email: "" as string | null,
	password: "" as string | null,
	confirm: "" as string | null,
});

// 设置背景图
const backgroundStyle = computed(() => ({
	width: "100vw",
	minHeight: "100vh",
	backgroundImage: `url(${backGroundImage()})`,
	backgroundSize: "cover",
	backgroundPosition: "center",
	backgroundRepeat: "no-repeat",
}));

// 检查当前页面属于安卓还是电脑端，并给出相应的背景
const backGroundImage = () => {
	const backgroundImageUrls = {
		PC: "http://img.netbian.com/file/2024/0612/001218jHkbd.jpg",
		Android: "http://img.netbian.com/file/2024/0528/195900g7Txz.jpg",
	};
	return checkDevice() === "PC"
		? backgroundImageUrls["PC"]
		: backgroundImageUrls["Android"];
};

const handleRegister = async () => {
	// 判断email是否为空并输出对应的结果
	if (userInfo.email === null || userInfo.email.trim() === "") {
		message.error("邮箱不能为空", 1);
		return;
	}
	// 判断邮箱格式
	if (!isValidEmail(userInfo.email)) {
		message.error("邮箱格式不正确", 1);
		return;
	}

	// 判断password是否为空并输出对应的结果
	if (userInfo.password === null || userInfo.password.trim() === "") {
		message.error("密码不能为空", 1);
		return;
	}
	if (userInfo.confirm === null || userInfo.confirm.trim() === "") {
		message.error("确认密码不能为空", 1);
		return;
	}
	// 开始注册用户
	try {
		const result = await register(userInfo);
		if (result.data.status === "error") {
			message.error(result.data.message);
			return;
		}
		message.success(result.data.message);
		// 用户注册成功，跳转登录界面
		router.push("/admin/login").then(() => {
		});
		return;
	} catch (error) {
		message.error("服务器错误");
	}
};
</script>
