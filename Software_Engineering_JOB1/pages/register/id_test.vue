<template>
  <view class="verification-container">
    <!-- 顶部状态栏 -->
    <view class="status-bar"></view>

    <!-- 背景图片 -->
    <image class="background-image" src="../../static/login/register_background.png"></image>

    <!-- 返回按钮 -->
    <view class="back-button" @click="handleBack">
      <text>❮</text>
    </view>

    <!-- 身份认证标题 -->
    <view class="header">
      <text class="header-text">身份认证</text>
    </view>

    <!-- 验证表单容器 -->
    <view class="form-container">
      <!-- 验证表单 -->
      <form @submit.prevent="handleVerify" ref="verificationForm" class="verification-form">
        <view class="form-item email-item">
          <view class="input-icon">
            <image src="../../static/icons/email.png" class="icon"></image>
          </view>
          <input v-model="verificationForm.email" placeholder="请输入教育邮箱" class="input" readonly />
          <button type="button" @click="sendVerificationCode" class="send-code-button">发送验证码</button>
        </view>
        <view class="form-item code-item">
          <view class="input-icon">
            <image src="../../static/icons/code.png" class="icon"></image>
          </view>
          <input v-model="verificationForm.code" placeholder="请输入验证码" class="input" />
        </view>
        <view class="form-item">
          <button type="primary" @click="handleVerify" class="verify-button">确认</button>
        </view>
      </form>
    </view>
  </view>
</template>

<script>
export default {
  name: "IdentityVerification",
  data() {
    return {
      verificationForm: {
        email: "",
        code: ""
      }
    };
  },
  created() {
    // 从上一个页面的参数中获取教育邮箱并自动填充
    const currentPage = getCurrentPages().pop();
    if (currentPage.options && currentPage.options.email) {
      this.verificationForm.email = currentPage.options.email;
    }
  },
  methods: {
    handleBack() {
      // 返回上一页逻辑
      uni.navigateBack();
    },
    sendVerificationCode() {
      if (this.verificationForm.email) {
        uni.request({
          url: 'https://734dw56037em.vicp.fun/users/send_verification_code/',  // Django后端API地址
          method: 'POST',
          data: JSON.stringify({
            email: this.verificationForm.email
          }),
          header: {
            'Content-Type': 'application/json'
          },
          success: (res) => {
            if (res.statusCode === 200) {
              uni.showToast({
                title: '验证码已发送',
                icon: 'none'
              });
            } else {
              uni.showToast({
                title: '发送失败：' + res.data.error,
                icon: 'none'
              });
            }
          },
          fail: () => {
            uni.showToast({
              title: '请求失败',
              icon: 'none'
            });
          }
        });
      } else {
        uni.showToast({
          title: '请输入教育邮箱',
          icon: 'none'
        });
      }
    },

    handleVerify() {
      if (this.verificationForm.email && this.verificationForm.code) {
        uni.request({
          url: 'https://734dw56037em.vicp.fun/users/verify_email/',  // Django后端API地址
          method: 'POST',
          data: JSON.stringify({
            email: this.verificationForm.email,
            code: this.verificationForm.code
          }),
          header: {
            'Content-Type': 'application/json'
          },
          success: (res) => {
            if (res.statusCode === 200) {
              uni.showToast({
                title: '验证成功',
                icon: 'none'
              });
              uni.navigateTo({
                url: '/pages/register/register_success'
              });
            } else {
              uni.showToast({
                title: '验证失败：' + res.data.error,
                icon: 'none'
              });
            }
          },
          fail: () => {
            uni.showToast({
              title: '请求失败',
              icon: 'none'
            });
          }
        });
      } else {
        uni.showToast({
          title: '请完整填写信息',
          icon: 'none'
        });
      }
    }

  }
};
</script>

<style scoped>
.verification-container {
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
  text-align: center;
}

.header-text {
  font-size: 1.8rem;
  font-weight: bold;
  color: #000;
}

.form-container {
  position: absolute;
  top: 224px;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  max-width: 321px;
  height: 50%;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.verification-form {
  width: 100%;
}

.form-item {
  margin-bottom: 20px;
  position: relative;
  display: flex;
  align-items: center;
}

.input {
  width: calc(100% - 40px);
  padding: 12px;
  border: none;
  border-bottom: 1px solid #ccc;
  font-size: 16px;
  background-color: transparent;
  padding-left: 40px;
}

.input-icon {
  position: absolute;
  left: 10px;
}

.icon {
  width: 20px;
  height: 20px;
}

.send-code-button {
  position: absolute;
  right: 10px;
  background-color: #A6D3F2;
  color: #000;
  padding: 2px 4px;

  border: none;
  border-radius: 20px;
  font-size: 14px;
}

.verify-button {
  position: absolute; /* 将按钮绝对定位 */
  bottom: -250px; /* 调整到屏幕底部的距离 */
  left: 50%; /* 使按钮的左边定位到页面的 50% 处 */
  transform: translateX(-50%); /* 使按钮在水平方向完全居中 */
  width: 70%;
  padding: 2px;
  background-color: #4095E5;
  color: #fff;
  border: none;
  border-radius: 20px;
  font-size: 18px;
}
</style>