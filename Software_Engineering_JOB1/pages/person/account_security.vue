<template>
  <view class="container">
    <!-- 页面标题 -->
<!--    <view class="header">
      <text class="title">账户安全</text>
    </view> -->

    <!-- 修改密码卡片 -->
    <view class="security-card">
      <text class="card-title">修改密码</text>
      <view class="form-item">
        <text class="label">当前密码</text>
        <input 
          v-model="currentPassword" 
          placeholder="请输入当前密码" 
          type="password" 
          class="input" 
        />
      </view>
      <view class="form-item">
        <text class="label">新密码</text>
        <input 
          v-model="newPassword" 
          placeholder="请输入新密码" 
          type="password" 
          class="input" 
        />
      </view>
      <view class="form-item">
        <text class="label">确认新密码</text>
        <input 
          v-model="confirmPassword" 
          placeholder="请确认新密码" 
          type="password" 
          class="input" 
        />
      </view>
      <button class="submit-button" @click="changePassword">提交修改</button>
    </view>

    <!-- 修改绑定邮箱卡片 -->
    <view class="security-card">
      <text class="card-title">修改绑定邮箱</text>
      <view class="form-item">
        <text class="label">新邮箱地址</text>
        <input 
          v-model="newEmail" 
          placeholder="请输入新的邮箱地址" 
          type="email" 
          class="input" 
        />
      </view>
      <button class="send-button" @click="sendVerificationEmail">发送验证邮件</button>
      <view class="form-item">
        <text class="label">验证码</text>
        <input 
          v-model="verificationCode" 
          placeholder="请输入收到的验证码" 
          type="text" 
          class="input" 
        />
      </view>
      <button class="submit-button" @click="changeEmail">确认更改</button>
    </view>

    <!-- 成功提示弹窗 -->
    <view v-if="showSuccess" class="success-popup">
      <image src="/static/icons/success.png" class="success-icon" />
      <text class="success-text">{{ successMessage }}</text>
      <button class="close-button" @click="closePopup">关闭</button>
    </view>
  </view>
</template>
<script>
export default {
  data() {
    return {
      // 修改密码相关数据
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',

      // 修改邮箱相关数据
      newEmail: '',
      verificationCode: '',

      // 成功提示
      showSuccess: false,
      successMessage: ''
    };
  },
  methods: {
    // 修改密码方法
    changePassword() {
      if (!this.currentPassword || !this.newPassword || !this.confirmPassword) {
        uni.showToast({
          title: '请填写所有密码字段',
          icon: 'none'
        });
        return;
      }
      if (this.newPassword !== this.confirmPassword) {
        uni.showToast({
          title: '新密码与确认密码不一致',
          icon: 'none'
        });
        return;
      }

      // 模拟密码修改
      console.log({
        currentPassword: this.currentPassword,
        newPassword: this.newPassword
      });

      // 清空表单
      this.currentPassword = '';
      this.newPassword = '';
      this.confirmPassword = '';

      // 显示成功提示
      this.successMessage = '密码修改成功！';
      this.showSuccess = true;
    },

    // 发送验证邮件方法
    sendVerificationEmail() {
      if (!this.newEmail) {
        uni.showToast({
          title: '请填写新的邮箱地址',
          icon: 'none'
        });
        return;
      }
      // 简单邮箱格式验证
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.newEmail)) {
        uni.showToast({
          title: '请输入有效的邮箱地址',
          icon: 'none'
        });
        return;
      }

      // 模拟发送验证邮件
      console.log({
        newEmail: this.newEmail
      });

      uni.showToast({
        title: '验证邮件已发送，请查收',
        icon: 'success'
      });
    },

    // 修改邮箱方法
    changeEmail() {
      if (!this.newEmail || !this.verificationCode) {
        uni.showToast({
          title: '请填写所有邮箱字段',
          icon: 'none'
        });
        return;
      }

      // 模拟邮箱修改
      console.log({
        newEmail: this.newEmail,
        verificationCode: this.verificationCode
      });

      // 清空表单
      this.newEmail = '';
      this.verificationCode = '';

      // 显示成功提示
      this.successMessage = '邮箱绑定成功！';
      this.showSuccess = true;
    },

    // 关闭成功提示弹窗
    closePopup() {
      this.showSuccess = false;
    }
  }
};
</script>



<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f2f5;
  padding: 40rpx 20rpx;
  min-height: 100vh;
  box-sizing: border-box;
}

/* 页面标题样式 */
.header {
  width: 100%;
  text-align: center;
  margin-bottom: 30rpx;
}

.title {
  font-size: 36rpx;
  font-weight: bold;
  color: #333333;
}

/* 安全卡片样式 */
.security-card {
  width: 100%;
  max-width: 800rpx;
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 30rpx 40rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.1);
  margin-bottom: 40rpx;
}

.card-title {
  font-size: 32rpx;
  font-weight: bold;
  color: #007aff;
  margin-bottom: 20rpx;
  text-align: center;
}

/* 表单项样式 */
.form-item {
  width: 100%;
  max-width: 800rpx; /* 与 .security-card 一致 */
  margin-bottom: 20rpx;
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 28rpx;
  font-weight: bold;
  color: #555555;
  margin-bottom: 10rpx;
}

/* 增加输入框高度 */
.input {
  width: 100%;
  max-width: 800rpx; /* 与 .security-card 一致 */
  height: 60rpx; /* 增加高度 */
  border: 1rpx solid #dddddd;
  border-radius: 10rpx;
  padding: 20rpx; /* 调整填充 */
  font-size: 26rpx;
  color: #333333;
  background-color: #f9f9f9;
  box-sizing: border-box;
}

/* 增加 textarea 高度 */
.textarea {
  width: 100%;
  height: 350rpx; /* 进一步增大高度 */
  min-height: 300rpx; /* 更新最小高度 */
  border: 1rpx solid #dddddd;
  border-radius: 10rpx;
  padding: 20rpx; /* 调整填充 */
  font-size: 26rpx;
  color: #333333;
  background-color: #f9f9f9;
  resize: vertical; /* 允许垂直方向调整高度 */
  box-sizing: border-box;
}

/* 按钮样式 */
.submit-button {
  width: 100%;
  max-width: 800rpx; /* 与 .security-card 一致 */
  height: 60rpx;
  background-color: #007aff;
  color: #ffffff;
  font-size: 28rpx;
  border: none;
  border-radius: 10rpx;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  margin-top: 10rpx;
}

.submit-button:hover {
  background-color: #005bb5;
  transform: scale(1.02);
}

.send-button {
  width: 100%;
  max-width: 800rpx;
  height: 60rpx;
  background-color: #34c759;
  color: #ffffff;
  font-size: 28rpx;
  border: none;
  border-radius: 10rpx;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  margin-top: 10rpx;
  margin-bottom: 20rpx;
}

.send-button:hover {
  background-color: #28a745;
  transform: scale(1.02);
}

/* 成功提示弹窗样式 */
.success-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 40rpx 30rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1000;
}

.success-icon {
  width: 80rpx;
  height: 80rpx;
  margin-bottom: 20rpx;
}

.success-text {
  font-size: 30rpx;
  color: #28a745;
  margin-bottom: 30rpx;
}

.close-button {
  width: 120rpx;
  height: 50rpx;
  background-color: #28a745;
  color: #ffffff;
  font-size: 26rpx;
  border: none;
  border-radius: 10rpx;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.close-button:hover {
  background-color: #1e7e34;
  transform: scale(1.02);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .container {
    padding: 20rpx;
  }

  .title {
    font-size: 32rpx;
  }

  .card-title {
    font-size: 28rpx;
  }

  .label {
    font-size: 24rpx;
  }

  .input,
  .send-button,
  .submit-button,
  .close-button {
    font-size: 24rpx;
  }

  .textarea {
    height: 220rpx; /* 略微减小以适应小屏设备 */
  }

  .submit-button {
    max-width: 100%;
  }
}
</style>
