<template>
  <view class="container">
    <!-- 顶部导航栏 -->
    <view class="navbar">
      <text
        v-for="(tab, index) in tabs"
        :key="index"
        :class="['navbar-tab', { active: activeTab === index }]"
        @click="switchTab(index)"
      >
        {{ tab }}
      </text>
    </view>
    <view class="navbar-line"></view>

    <!-- 上传和下载按钮 -->
    <view class="button-container">
      <button class="upload-button" @click="openFile">上传</button>
      <!-- <button class="download-button" @click="downloadFile">下载</button> -->
    </view>

    <view class="content-container">
      <!-- 文件列表 -->
      <scroll-view class="file-list-box" scroll-y="true">
        <view class="section-header">
          <text class="section-title">文件列表</text>
        </view>
        <view class="file-item" v-for="(file, index) in files" :key="file.id"> 
          <text class="file-name">{{ file.file_name }}</text>
          <button class="delete-button" @click="deleteFile(file.id)" v-if="isUploader(file.uploaded_by)">删除</button>
        </view>
      </scroll-view>

      <!-- 项目描述 -->
      <scroll-view class="description-box" scroll-y="true">
        <view class="section-header">
          <text class="section-title">项目描述</text>
        </view>
        <text class="description-text">{{ description }}</text>
      </scroll-view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      tabs: ['项目信息', '项目成员', '项目设置'],
      activeTab: 0,
      files: [],  // 初始化为空
      description: '这是项目的描述内容，可以随着内容的增加而滚动查看。',
      projectId: '' // 存储项目 ID
    };
  },
  onLoad(options) {
    this.projectId = options.id; // 从页面参数获取项目 id
    console.log('Project ID:', this.projectId); // 输出查看
    this.getProjectFiles(); // 获取项目文件
  },
  methods: {
    switchTab(index) {
        this.activeTab = index; 
        if (index === 1) {
          uni.redirectTo({
            url: `/pages/home/teammate?id=${this.projectId}`, // 将 projectId 传递给 teammate 页面
          });
        } else if (index === 2) {
          uni.redirectTo({
            url: `/pages/home/project_setting?id=${this.projectId}`, // 将 projectId 传递给 project_setting 页面
          });
        }
      },
    
    // 获取项目文件列表
    async getProjectFiles() {
      try {
        const token = uni.getStorageSync('authToken'); // 获取存储的 token
        const response = await uni.request({
          url: `https://734dw56037em.vicp.fun/projects/files/?project_id=${this.projectId}`, // 获取项目文件
          method: 'GET',
          header: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });
        // 处理后端返回的数据
        if (response.statusCode === 200) {
          console.log(response.data);
          this.files = response.data;  // 假设后端返回的数据是文件的列表
        } else {
          console.error('获取文件失败:', response.data);
        }
      } catch (error) {
        console.error('获取文件失败:', error);
      }
    },
    
    // 打开文件选择器并输入文件名
    openFile() {
      uni.chooseFile({
        count: 1, // 选择文件的数量
        extensions: ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx', '.xls', '.xlsx'], // 允许的文件扩展名
        success: (res) => {
          console.log('选择的文件:', res); // 输出选择的文件信息
          if (res.tempFiles && res.tempFiles.length > 0) { // 检查 tempFiles 是否存在且不为空
            const file = res.tempFiles[0];
            console.log(file);
            if (file.size / 1024 / 1024 > 20) { // 限制文件大小
              uni.showToast({
                title: '附件大小不能超过20M',
                icon: 'none',
              });
              return;
            }
            
            // 弹窗让用户输入文件名
            uni.showModal({
              title: '输入文件名',
              content: '请输入文件名（包括扩展名，例如: example.txt）',
              editable: true,  // 允许用户输入
              success: (inputRes) => {
                if (inputRes.confirm && inputRes.content) {
                  const customFileName = inputRes.content.trim(); // 用户输入的文件名
                  console.log('用户输入的文件名:', customFileName);
                  this.uploadFile(file.path, customFileName); // 上传文件，并传递用户输入的文件名
                } else {
                  console.log('用户取消或未输入文件名');
                }
              },
              fail: (err) => {
                console.error('文件名输入失败:', err);
              }
            });
          } else {
            console.error('未选择任何文件');
          }
        },
        fail: (err) => {
          console.error('选择文件失败:', err);
        }
      });
    },
    
    // 上传文件
    uploadFile(filePath, customFileName) {
      if (!customFileName) {
        uni.showToast({
          title: '文件名不能为空',
          icon: 'none',
        });
        return;
      }

      console.log('准备上传的文件路径:', filePath);
      console.log('用户输入的文件名:', customFileName);

      uni.uploadFile({
        url: 'https://734dw56037em.vicp.fun/projects/files/', // 后端上传接口
        filePath: filePath,
        name: 'file',  // 后端接收的字段名
        formData: {
          project: this.projectId, // 项目ID
          file_name: customFileName // 传递用户输入的文件名
        },
        header: {
          'Authorization': `Token ${uni.getStorageSync('authToken')}`
        },
        success: (res) => {
          console.log('上传成功:', res);
          this.getProjectFiles(); // 重新获取文件列表
        },
        fail: (err) => {
          console.error('上传失败:', err);
        }
      });
    },

    // 删除文件
    async deleteFile(fileId) {
      try {
        const token = uni.getStorageSync('authToken'); // 获取存储的 token
        const response = await uni.request({
          url: `https://734dw56037em.vicp.fun/projects/files/${fileId}/`, // 删除文件的接口
          method: 'DELETE',
          header: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });

        if (response.statusCode === 204) {
          console.log('文件删除成功');
          this.getProjectFiles(); // 重新获取文件列表
        } else {
          console.error('删除文件失败:', response.data);
        }
      } catch (error) {
        console.error('删除文件失败:', error);
      }
    },

    // 检查用户是否为文件上传者
    isUploader(uploadedBy) {
      const currentUserId = uni.getStorageSync('currentUserId'); // 获取当前用户 ID
      return uploadedBy === currentUserId;
    }
  }
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  background-color: #f0f4f7;
  padding: 0;
  height: 100vh;
}

/* 顶部导航栏样式 */
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #ffffff;
  padding-top: 20rpx;
  padding-bottom: 20rpx;
}

.navbar-tab {
  font-size: 32rpx;
  color: #666;
  cursor: pointer;
}

.navbar-tab.active {
  color: #007aff;
  font-weight: bold;
}

.navbar-line {
  width: 100%;
  height: 2rpx;
  background-color: #e0e0e0;
}

/* 上传和下载按钮样式 */
.button-container {
  display: flex;
  justify-content: space-around;
  margin: 20rpx auto;
  width: 80%;
}

.upload-button,
.download-button {
  background-color: #007aff;
  color: #fff;
  border: none;
  border-radius: 12rpx;
  padding: 20rpx 40rpx;
  font-size: 32rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  cursor: pointer;
  width: 40%;
}

/* 内容区域样式 */
.content-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
  width: 80%;
}

/* 区域标题样式 */
.section-header {
  border-bottom: 1rpx solid #e0e0e0;
  padding-bottom: 10rpx;
  margin-bottom: 10rpx;
}

.section-title {
  font-size: 34rpx;
  font-weight: bold;
  color: #333;
}

/* 文件列表样式 */
.file-list-box {
  width: 100%;
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 20rpx;
  margin-bottom: 10rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  flex: 1;
}

.file-item {
  padding: 10rpx 0;
  border-bottom: 1rpx solid #e0e0e0;
}

.file-name {
  font-size: 28rpx;
  color: #333;
}

/* 项目描述样式 */
.description-box {
  width: 100%;
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 20rpx;
  margin-top: 10rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  flex: 1;
}

.description-text {
  font-size: 28rpx;
  color: #666;
  line-height: 1.5;
}

.delete-button {
  margin-left: 10px; /* 在文件名和删除按钮之间添加间距 */
  background-color: red; /* 添加背景色以方便查看 */
  color: white; /* 设置字体颜色 */
}

</style>