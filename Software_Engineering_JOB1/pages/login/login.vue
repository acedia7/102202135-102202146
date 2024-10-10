<template>
  <view class="login-container">
    <!-- 顶部状态栏 -->
<!--  <StatusBar /> -->
    <!-- 底层背景图片 -->
    <image class="background-image" src="../../static/login/login1.png"></image>
    
    <!-- 圆角矩形框 -->
    <view class="rounded-box">
      <view class="header">
        <text class="header-text">Hi~</text>
      </view>
      <form @submit.prevent="handleLogin" ref="loginForm" class="login-form">
        <view class="form-item username-item">
          <view class="input-icon">
            <image src="../../static/icons/user-icon.png" class="icon"></image>
          </view>
          <input v-model="loginForm.username" placeholder="请输入账号" class="input" />
        </view>
        <view class="form-item password-item">
          <view class="input-icon">
            <image src="../../static/icons/lock-icon.png" class="icon"></image>
          </view>
          <input v-model="loginForm.password" type="password" placeholder="请输入密码" class="input" />
        </view>
        <view class="extra-links">
          <navigator url="/pages/register/register" class="link">注册</navigator>
          <navigator url="/pages/forgot-password/forgot-password" class="link forgot-password">忘记密码</navigator>
        </view>
        <view class="form-item">
          <button type="primary" @click.prevent="handleLogin" class="login-button">登录</button>
        </view>
      </form>
    </view>
		<checkbox-group @change="handleAgreementChange" class="agreement-container">
		  <label class="checkbox-label">
		    <checkbox value="agree" class="checkbox">
		    请勾选
		    <navigator url="/pages/user-agreement/user-agreement" class="link">用户使用协议</navigator>
			</checkbox>
		  </label>
		</checkbox-group>
  </view>
</template>

<script>
import StatusBar from "@/components/StatusBar.vue";
export default {
  name: "LoginPage",
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      agreementChecked: false
    };
  },
  methods: {
    handleAgreementChange(event) {
      this.agreementChecked = event.detail.value.includes('agree');
    },
    handleLogin() {
      console.log(this.agreementChecked);

      if (!this.agreementChecked) {
        uni.showToast({
          title: '请勾选用户使用协议',
          icon: 'none'
        });
        return;
      }

      if (!this.loginForm.username || !this.loginForm.password) {
        uni.showToast({
          title: '请完整填写信息',
          icon: 'none'
        });
        return;
      }

      // 发送POST请求到后端登录接口
      uni.request({
        url: 'https://734dw56037em.vicp.fun/users/login/',  // 后端Django的登录接口URL
        method: 'POST',
        header: {
          'Content-Type': 'application/json'  // 设置请求头
        },
        data: {
          email: this.loginForm.username,  // 假设登录时用的是邮箱作为用户名
          password: this.loginForm.password
        },
        success: (res) => {
          if (res.statusCode === 200) {
            // 登录成功，获取token
            this.getAuthToken();
          } else {
            uni.showToast({
              title: res.data.error || '登录失败',
              icon: 'none'
            });
          }
        },
        fail: (err) => {
          uni.showToast({
            title: '请求失败，请稍后再试',
            icon: 'none'
          });
          console.error(err);
        }
      });
    },
    getAuthToken() {
      uni.request({
        url: 'https://734dw56037em.vicp.fun/api-token-auth/',  // 获取token的接口URL
        method: 'POST',
        header: {
          'Content-Type': 'application/json'
        },
        data: {
          username: this.loginForm.username,
          password: this.loginForm.password
        },
        success: (res) => {
          if (res.statusCode === 200 && res.data.token) {
            // 保存token到本地
            uni.setStorageSync('authToken', res.data.token);
			const token = uni.getStorageSync('authToken');
			console.log('保存的 token:', token); // 在控制台查看 token
            // 登录成功，跳转到主页
            uni.showToast({
              title: '登录成功',
              icon: 'success'
            });
            uni.switchTab({
              url: '/pages/home/home'  // 跳转到首页
            });
          } else {
            uni.showToast({
              title: res.data.error || '获取token失败',
              icon: 'none'
            });
          }
        },
        fail: (err) => {
          uni.showToast({
            title: '请求失败，请稍后再试',
            icon: 'none'
          });
          console.error(err);
        }
      });
    }
  }
};
</script>



<style scoped>
.login-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.status-bar {
  height: 57px;
  background-color: transparent;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.rounded-box {
  position: absolute;
  top: 208px;
  left: 50%;
  transform: translateX(-50%);
  width: 300px;
  height: 437px;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.header-text {
  font-size: 2rem;
  font-weight: bold;
}

.login-form {
  width: 100%;
}

.form-item {
  margin-bottom: 15px;
  position: relative;
  display: flex;
  align-items: center;
}

.input {
  width: calc(100% - 40px);
  padding: 10px;
  padding-left: 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.input-icon {
  position: absolute;
  left: 10px;
}

.icon {
  width: 20px;
  height: 20px;
}

.extra-links {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  width: 100%;
}

.link {
  color: #007aff;
}

.forgot-password {
  color: #aaa;
}

.checkbox {
  margin-right: 10px;
  text-align: center;
}

.login-button {
  width: 80%;
  padding: 8px;
  background-color: #007aff;
  color: #fff;
  border: none;
  border-radius: 5px;
}

.agreement-container {
  margin-top: 620px;
  width: 300px;
  text-align: center;
  z-index: 99;
}
</style>