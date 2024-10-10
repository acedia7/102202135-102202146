<template>
  <view class="register-container">
    <!-- 顶部状态栏 -->
    <view class="status-bar"></view>

    <!-- 背景图片 -->
    <image class="background-image" src="../../static/login/register_background.png"></image>

    <!-- 返回按钮 -->
    <view class="back-button" @click="handleBack">
      <text>❮</text>
    </view>

    <!-- 注册标题 -->
    <view class="header">
      <text class="header-text">新用户注册</text>
    </view>

    <!-- 注册表单 -->
    <form @submit.prevent="handleRegister" ref="registerForm" class="register-form">
      <view class="form-item">
        <input v-model="registerForm.name" placeholder="请输入姓名" class="input" />
      </view>
      <view class="form-item">
        <input v-model="registerForm.school" placeholder="请输入学校" class="input" />
      </view>
	  <view class="form-item">
	    <input v-model="registerForm.email" placeholder="请输入教育邮箱" class="input" />
	  </view>
      <view class="form-item">
        <input v-model="registerForm.studentId" placeholder="请输入学号" class="input" />
      </view>
      <view class="form-item">
        <input v-model="registerForm.password" type="password" placeholder="请输入密码" class="input" />
      </view>
      <view class="form-item">
        <input v-model="registerForm.confirmPassword" type="password" placeholder="请再次确认密码" class="input" />
      </view>
      <view class="form-item">
        <button type="primary" @click="handleRegister" class="register-button">确认</button>
      </view>
    </form>
  </view>
</template>

<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      registerForm: {
        name: "",
        school: "",
        email: "",
        studentId: "",
        password: "",
        confirmPassword: ""
      }
    };
  },
  methods: {
    handleBack() {
      // 返回上一页逻辑
      uni.navigateBack();
    },
    handleRegister() {
      if (this.registerForm.password !== this.registerForm.confirmPassword) {
        uni.showToast({
          title: '两次输入的密码不一致',
          icon: 'none'
        });
        return;
      }

      // 发送注册请求到后端
      uni.request({
        url: 'https://734dw56037em.vicp.fun/users/register/',  // 后端注册接口URL
        method: 'POST',
        header: {
          'Content-Type': 'application/json'
        },
        data: {
          name: this.registerForm.name,
          school: this.registerForm.school,
          student_id: this.registerForm.studentId,
          password: this.registerForm.password,
          password_confirm: this.registerForm.confirmPassword,
          email: this.registerForm.email
        },
        success: (res) => {
          if (res.statusCode === 200 || res.statusCode === 201) {
            uni.showToast({
              title: res.data.message,
              icon: 'success'
            });
            // 跳转到发送验证码的页面
            uni.navigateTo({
              url: `/pages/register/id_test?email=${this.registerForm.email}`
            });
          } else {
            uni.showToast({
              title: res.data.error || '注册失败',
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
  }  // 这里不要添加分号
};
</script>



<style scoped>
.register-container {
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

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  font-size: 24px;
  color: #000;
  z-index: 1;
}

.header {
  margin-top: 60px;
  margin-left: -110px;
  text-align: center;
}

.header-text {
  font-size: 1.8rem;
  font-weight: bold;
  color: #000;
}

.register-form {
  width: 70%;
  margin-top: 50px;
}

.form-item {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
}

.input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 20px;
  font-size: 16px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.register-button {
  width: 50%;
  padding: 2px;
  background-color: #4095E5;
  color: #fff;
  border: none;
  border-radius: 20px;
  font-size: 20px;
  position: absolute;
  bottom: 125px;
  left: 50%;
  transform: translateX(-50%);
}
</style>