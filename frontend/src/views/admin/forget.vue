<template>
	<a-card :style="backgroundStyle">
		<a-flex justify="center" style="margin-top: 20vh">
			<a-space direction="vertical" size="middle" style="width: 300px">
				<a-typography-title style="padding-left: 5px"
				><strong>Forget</strong></a-typography-title
				>
				<a-input v-model:value="userInfo.email" type="email" placeholder="请输入邮箱"/>
				<span>
          <a-typography-link href="/user/login" style="float: right"
          >返回登录</a-typography-link
          >
        </span>

				<a-button type="primary" @click="handleLogin" style="width: 300px"
				>发送邮件
				</a-button
				>
			</a-space>
		</a-flex>
	</a-card>
</template>

<script lang="ts" setup>
import {reactive, computed} from "vue";
import {message} from "ant-design-vue";
import {isValidEmail} from "@/utils/tools";
import {login} from "@/api/user";
import {useRoute, useRouter} from "vue-router";
import {checkDevice} from "@/utils/tools";

const userInfo: object = reactive({
	email: "" as string | null,
});

const route = useRoute();
const router = useRouter();

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

const handleLogin = async () => {
	// 判断 email 是否为空并输出对应的结果
	if (userInfo.email === null || userInfo.email.trim() === "") {
		message.error("邮箱不能为空", 1);
		return;
	}

	// 判断邮箱格式
	if (!isValidEmail(userInfo.email.trim())) {
		message.error("邮箱格式不正确", 1);
		return;
	}

	// 判断 password 是否为空并输出对应的结果
	if (userInfo.password === null || userInfo.password.trim() === "") {
		message.error("密码不能为空", 1);
		return;
	}

	// 开始登录用户
	try {
		const result = await login(userInfo);
		if (result.data.status === "error") {
			message.error(result.data.message);
			return;
		}

		// 保存用户信息
		const token = result.data.result.token;
		const ResponseUserInfo = result.data.result.userInfo;
		localStorage.removeItem("token");
		localStorage.removeItem("user");
		localStorage.setItem("token", token);
		localStorage.setItem("userInfo", JSON.stringify(ResponseUserInfo));
		message.success(result.data.message);

		// 获取重定向路径
		const redirect = route.query.redirect || "/back";
		router.push(redirect as string);

		return;
	} catch (error) {
		message.error("服务器错误");
	}
};
</script>
