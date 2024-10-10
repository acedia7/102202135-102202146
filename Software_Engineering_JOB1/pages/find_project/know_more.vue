<template>
  <view class="container">
    <!-- 项目图片 -->
    <!-- 确保文件扩展名为 .jpg -->
    <image
      class="project-image"
      src="/static/photo/project1.jpg"
      mode="aspectFill"
      @load="onImageLoad"
      :style="{ opacity: imageLoaded ? 1 : 0, animation: imageLoaded ? 'fadeIn 0.5s forwards' : 'none' }"
    />
    
    <!-- 项目名字 -->
    <view class="project-name" v-if="imageLoaded" :style="{ animation: 'slideUp 0.5s forwards' }">
      {{ project.name }}
    </view>
    
    <!-- 项目信息 -->
    <view class="project-details" v-if="imageLoaded">
      <!-- 项目编号 -->
      <view class="detail-item" :style="{ animation: 'slideUp 0.5s forwards ' + delayAnimation(0) }">
        <text class="detail-title">项目编号：</text>
        <text class="detail-content">{{ project.number }}</text>
      </view>
      <view class="separator"></view>
      
      <!-- 项目状态 -->
      <view class="detail-item" :style="{ animation: 'slideUp 0.5s forwards ' + delayAnimation(1) }">
        <text class="detail-title">项目状态：</text>
        <text class="detail-content">{{ project.status }}</text>
      </view>
      <view class="separator"></view>
      
      <!-- 项目领域 -->
      <view class="detail-item" :style="{ animation: 'slideUp 0.5s forwards ' + delayAnimation(2) }">
        <text class="detail-title">项目领域：</text>
        <text class="detail-content">{{ project.field }}</text>
      </view>
      <view class="separator"></view>
      
      <!-- 项目描述 -->
      <view class="detail-item" :style="{ animation: 'slideUp 0.5s forwards ' + delayAnimation(3) }">
        <text class="detail-title">项目描述：</text>
        <text class="detail-content">{{ project.description }}</text>
      </view>
      <view class="separator"></view>
      
      <!-- 创建日期 -->
      <view class="detail-item" :style="{ animation: 'slideUp 0.5s forwards ' + delayAnimation(4) }">
        <text class="detail-title">创建日期：</text>
        <text class="detail-content">{{ project.date }}</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      imageLoaded: false,
      project: {
        name: '项目名称一',
        number: 'P001',
        status: '进行中',
        field: '金融科技',
        description: '这是一个关于金融科技领域的项目，旨在通过创新技术提升金融服务的效率和安全性。',
        date: '2024-01-15',
      },
    };
  },
  methods: {
    onImageLoad() {
      this.imageLoaded = true;
    },
    delayAnimation(index) {
      return `${0.3 + index * 0.2}s`;
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: #f5f5f5;
  height: 100vh;
  overflow-y: auto;
}

.project-image {
  width: 100%;
  height: 250px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.project-name {
  margin-top: 20px;
  font-size: 28px;
  font-weight: bold;
  color: #333333;
  text-align: center;
}

.project-details {
  margin-top: 20px;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.detail-item {
  margin-bottom: 15px;
}

.detail-title {
  font-size: 18px;
  font-weight: bold;
  color: #555555;
  margin-bottom: 5px;
  display: block;
}

.detail-content {
  font-size: 16px;
  color: #666666;
  display: block;
}

.separator {
  height: 1px;
  background-color: #e0e0e0;
  margin: 10px 0;
}

/* 动画效果 */
@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* 响应式设计 */
@media (min-width: 768px) {
  .project-image {
    height: 300px;
  }
  
  .project-name {
    font-size: 32px;
  }
  
  .detail-title {
    font-size: 20px;
  }
  
  .detail-content {
    font-size: 18px;
  }
}
</style>
