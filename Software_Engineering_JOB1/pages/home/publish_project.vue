<template>
  <view class="container">
    <!-- 上传项目代表图片 -->
    <view class="form-item animated fadeInUp delay-0.5s">
      <text class="label">请上传一张最能代表你们项目的图片</text>
      <view class="upload-container" @click="chooseImage">
        <image v-if="projectImage" :src="projectImage" class="uploaded-image" />
        <view v-else class="upload-placeholder">
          <image src="/static/icons/upload.png" class="upload-icon" />
          <text class="upload-text">点击上传图片</text>
        </view>
      </view>
    </view>

    <!-- 项目名称 -->
    <view class="form-item animated fadeInUp delay-1s">
      <text class="label">项目名称</text>
      <input class="input" placeholder="请输入项目名称" v-model="projectName" />
    </view>

    <!-- 项目描述 -->
    <view class="form-item animated fadeInUp delay-1.5s">
      <text class="label">项目描述</text>
      <textarea
        class="textarea"
        placeholder="请输入项目描述"
        v-model="projectDescription"
        :maxlength="500"
        auto-height
        show-count
      />
    </view>

    <!-- 项目领域 -->
    <view class="form-item animated fadeInUp delay-2s">
      <text class="label">项目领域</text>
      <input class="input" placeholder="请输入项目领域" v-model="projectField" />
    </view>

    <!-- 开源许可选择 -->
    <view class="form-item animated fadeInUp delay-2.5s">
      <text class="label">开源许可</text>
      <picker mode="selector" :range="licenses" v-model="licenseIndex" @change="onLicenseChange">
        <view class="picker">
          <text class="picker-text">{{ licenses[licenseIndex] }}</text>
          <image src="/static/icons/arrow_down.png" class="arrow-icon" />
        </view>
      </picker>
    </view>

    <!-- 公开或隐私选择 -->
    <view class="form-item animated fadeInUp delay-3s">
      <text class="label">项目可见性</text>
      <view class="visibility-options">
        <view
          class="option"
          :class="{ active: visibility === 'public' }"
          @click="setVisibility('public')"
        >
          <image class="icon" src="/static/icons/public.png" />
          <text>公开</text>
        </view>
        <view
          class="option"
          :class="{ active: visibility === 'private' }"
          @click="setVisibility('private')"
        >
          <image class="icon" src="/static/icons/private.png" />
          <text>隐私</text>
        </view>
      </view>
    </view>

    <!-- 确认发布按钮 -->
    <button class="submit-button animated fadeInUp delay-3.5s" @click="submitProject">
      确认发布
    </button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      projectImage: '', // 存储上传的项目图片
      projectName: '',
      projectDescription: '',
      projectField: '',
      licenses: ['GPL', 'MPL', 'BSD', 'MIT', 'Apache'],
      licenseIndex: 0,
      visibility: 'public',
    };
  },
  methods: {
    // 处理开源许可选择
    onLicenseChange(e) {
      this.licenseIndex = e.detail.value;
    },
    // 设置项目可见性
    setVisibility(type) {
      this.visibility = type;
    },
    // 选择并上传图片
    chooseImage() {
      uni.chooseImage({
        count: 1,
        sizeType: ['compressed'],
        sourceType: ['album', 'camera'],
        success: (res) => {
          const tempFilePath = res.tempFilePaths[0];
          if (tempFilePath) {
            this.projectImage = tempFilePath;
            console.log("选中的图片路径:", tempFilePath); // 打印图片路径，确保是本地路径
          } else {
            console.error("未获取到有效的图片路径");
          }
        },
        fail: () => {
          uni.showToast({
            title: '未选择图片',
            icon: 'none',
          });
        },
      });
    },
    // 提交项目
    submitProject() {
      // 验证输入
      if (!(this.projectName && this.projectDescription && this.projectField && this.projectImage)) {
        uni.showToast({
          title: '请完整填写信息并上传图片',
          icon: 'none',
        });
        return;
      }

      const is_private = this.visibility === 'private' ? 'True' : 'False';
      const token = uni.getStorageSync('authToken');

      // 获取文件名并处理长度
      const fileName = this.projectImage.split('/').pop(); // 获取文件名
      const maxFileNameLength = 100; // 最大文件名长度
      let newFileName = fileName;

      // 如果文件名超过最大长度，截取文件名
      if (newFileName.length > maxFileNameLength) {
        newFileName = newFileName.substring(0, maxFileNameLength);
        console.warn(`文件名长度超出限制，已截取为: ${newFileName}`);
      }

      // 使用 uni.uploadFile 上传文件
      uni.uploadFile({
        url: 'https://734dw56037em.vicp.fun/projects/projects/',
        filePath: this.projectImage, // 选择的图片路径
        name: 'image', // 文件的字段名为 image
        formData: {
          project_name: this.projectName,
          description: this.projectDescription,
          field: this.projectField,
          license: this.licenses[this.licenseIndex],
          is_private: is_private,
          status: 'preparing',
          file_name: newFileName, // 将新文件名添加到表单数据
        },
        header: {
          'Authorization': `Token ${token}`,
        },
        success: (res) => {
          console.log("服务器响应:", res.data); // 打印服务器响应数据
          if (res.statusCode === 201) {
            this.handleSuccess();
          } else {
            this.handleError(res.data.error || '项目发布失败');
          }
        },
        fail: (err) => {
          console.error("请求失败的详细信息:", err); // 打印失败详细信息
          this.handleError('请求失败，请稍后再试');
        },
      });
    },
    handleSuccess() {
      uni.showToast({
        title: '项目发布成功',
        icon: 'success',
        duration: 2000,
        success: () => {
          setTimeout(() => {
            uni.switchTab({
              url: '/pages/home/home',
            });
          }, 2000);
        },
      });
    },
    handleError(errorMsg) {
      uni.showToast({
        title: errorMsg || '项目发布失败',
        icon: 'none',
      });
    },
  },
};
</script>


<style scoped>
/* 定义动画关键帧 */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 动画类 */
.animated {
  animation-duration: 1s;
  animation-fill-mode: both;
}

.fadeInDown {
  animation-name: fadeInDown;
}

.fadeInUp {
  animation-name: fadeInUp;
}

.delay-0.5s {
  animation-delay: 0.5s;
}

.delay-1s {
  animation-delay: 1s;
}

.delay-1.5s {
  animation-delay: 1.5s;
}

.delay-2s {
  animation-delay: 2s;
}

.delay-2.5s {
  animation-delay: 2.5s;
}

.delay-3s {
  animation-delay: 3s;
}

.delay-3.5s {
  animation-delay: 3.5s;
}

/* 容器样式 */
.container {
  padding: 40rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* 移除背景颜色和渐变 */
  background-color: transparent;
  min-height: 100vh;
  box-sizing: border-box;
  position: relative;
}

/* 上传图片区域样式 */
.upload-container {
  width: 100%;
  max-width: 600rpx;
  height: 300rpx;
  border: 2rpx dashed #ccc;
  border-radius: 12rpx;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: border-color 0.3s, background-color 0.3s;
  position: relative;
}

.upload-container:hover {
  border-color: #007aff;
  background-color: #f0f8ff;
}

.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #666666;
}

.upload-icon {
  width: 80rpx;
  height: 80rpx;
  margin-bottom: 10rpx;
  animation: bounce 2s infinite;
}

.upload-text {
  font-size: 28rpx;
}

.uploaded-image {
  width: 100%;
  height: 100%;
  border-radius: 12rpx;
  object-fit: cover;
  transition: transform 0.3s, box-shadow 0.3s;
}

.uploaded-image:hover {
  transform: scale(1.05);
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.2);
}

/* 弹跳动画 */
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10rpx);
  }
  60% {
    transform: translateY(-5rpx);
  }
}

/* 项目名称和其他表单项样式 */
.form-item {
  width: 100%;
  max-width: 600rpx;
  margin-bottom: 40rpx;
}

.label {
  font-size: 34rpx;
  font-weight: bold;
  margin-bottom: 20rpx;
  display: block;
  color: #333333;
  text-shadow: 1rpx 1rpx 2rpx rgba(0, 0, 0, 0.05);
}

.input,
.textarea {
  width: 100%;
  padding: 20rpx;
  border: 1rpx solid #ccc;
  border-radius: 12rpx;
  font-size: 30rpx;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.input:focus,
.textarea:focus {
  border-color: #007aff;
  box-shadow: 0 0 10rpx rgba(0, 122, 255, 0.2);
}

.textarea {
  height: 200rpx;
  resize: none;
  overflow-y: auto;
}

.picker {
  width: 100%;
  padding: 20rpx;
  border: 1rpx solid #ccc;
  border-radius: 12rpx;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #ffffff;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.picker:hover {
  border-color: #007aff;
}

.picker-text {
  font-size: 30rpx;
  color: #333333;
}

.arrow-icon {
  width: 24rpx;
  height: 24rpx;
}

.visibility-options {
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-width: 600rpx;
}

.option {
  flex: 1;
  align-items: center;
  justify-content: center;
  padding: 20rpx;
  border: 1rpx solid #ccc;
  border-radius: 12rpx;
  margin-right: 20rpx;
  transition: background-color 0.3s, border-color 0.3s, transform 0.3s;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}

.option:last-child {
  margin-right: 0;
}

.option.active {
  border-color: #007aff;
  background-color: #e6f0ff;
  transform: scale(1.05);
}

.option:hover {
  background-color: #f0f8ff;
}

.icon {
  width: 80rpx;
  height: 80rpx;
  margin-bottom: 10rpx;
  transition: transform 0.3s;
}

.option:hover .icon {
  transform: rotate(10deg);
}

.option text {
  margin-top: 10rpx;
  font-size: 28rpx;
  color: #333;
  transition: color 0.3s;
}

.option:hover text {
  color: #007aff;
}

/* 确认发布按钮样式 */
.submit-button {
  width: 100%;
  max-width: 600rpx;
  padding: 20rpx;
  background-color: #007aff;
  color: #fff;
  border: none;
  border-radius: 12rpx;
  text-align: center;
  font-size: 34rpx;
  margin-top: 50rpx;
  transition: background-color 0.3s, transform 0.2s, box-shadow 0.3s;
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.1);
}

.submit-button:hover {
  background-color: #005bb5;
  box-shadow: 0 6rpx 16rpx rgba(0, 0, 0, 0.2);
}

.submit-button:active {
  transform: scale(0.95);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .container {
    padding: 20rpx;
  }

  .form-item {
    margin-bottom: 30rpx;
  }

  .label {
    font-size: 28rpx;
  }

  .input,
  .textarea {
    font-size: 24rpx;
    padding: 15rpx;
  }

  .picker-text {
    font-size: 24rpx;
  }

  .arrow-icon {
    width: 20rpx;
    height: 20rpx;
  }

  .option {
    padding: 15rpx;
    margin-right: 10rpx;
  }

  .icon {
    width: 60rpx;
    height: 60rpx;
  }

  .option text {
    font-size: 24rpx;
  }

  .submit-button {
    font-size: 28rpx;
    padding: 15rpx;
  }

  .qr-code-container {
    height: 250rpx;
  }

  .qr-code {
    width: 300rpx;
    height: 300rpx;
  }
}
</style>
