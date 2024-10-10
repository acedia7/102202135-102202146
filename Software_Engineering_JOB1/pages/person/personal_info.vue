<template>
  <view class="container">
    <!-- 头像部分 -->
    <view class="avatar-section">
      <image :src="avatar" class="avatar" @click="uploadAvatar"></image>
    </view>

    <!-- 个人信息部分 -->
    <scroll-view class="info-section" scroll-y>
      <!-- 姓名 -->
      <view class="info-item">
        <text class="label">姓名：</text>
        <text class="value">{{ form.name }}</text>
      </view>

      <!-- 学校 -->
      <view class="info-item">
        <text class="label">学校：</text>
        <text class="value">{{ form.school }}</text>
      </view>

      <!-- 专业 -->
      <view class="info-item" @click="toggleEdit('major')">
        <text class="label">专业：</text>
        <input 
          v-if="editField === 'major'" 
          v-model="form.major" 
          class="input" 
          @blur="toggleEdit('major')" 
          placeholder="请输入专业"
          :focus="editField === 'major'"
        />
        <text v-else class="value">{{ form.major }}</text>
      </view>

      <!-- 电话号码 -->
      <view class="info-item" @click="toggleEdit('phone')">
        <text class="label">电话：</text>
        <input 
          v-if="editField === 'phone'" 
          v-model="form.phone" 
          class="input" 
          type="number" 
          @blur="toggleEdit('phone')" 
          placeholder="请输入电话"
          :focus="editField === 'phone'"
        />
        <text v-else class="value">{{ form.phone }}</text>
      </view>

      <!-- 兴趣领域 -->
      <view class="info-item" @click="toggleEdit('interests')">
        <text class="label">兴趣领域：</text>
        <input 
          v-if="editField === 'interests'" 
          v-model="form.interests" 
          class="input" 
          @blur="toggleEdit('interests')" 
          placeholder="请输入兴趣领域"
          :focus="editField === 'interests'"
        />
        <text v-else class="value">{{ form.interests }}</text>
      </view>

      <!-- 空闲时间 -->
      <view class="info-item" @click="toggleEdit('freeTime')">
        <text class="label">空闲时间：</text>
        <input 
          v-if="editField === 'freeTime'" 
          v-model="form.freeTime" 
          class="input" 
          @blur="toggleEdit('freeTime')" 
          placeholder="请输入空闲时间"
          :focus="editField === 'freeTime'"
        />
        <text v-else class="value">{{ form.freeTime }}</text>
      </view>
    </scroll-view>

    <!-- 确认修改按钮 -->
    <view class="button-container">
      <button class="confirm-button" @click="confirmEdit">确认修改</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      avatar: '/static/default-avatar.png', // 默认头像
      editField: '', // 当前编辑的字段
      form: {
        name: '', // 姓名
        school: '', // 学校
        major: '', // 专业
        phone: '', // 电话
        interests: '', // 兴趣领域
        freeTime: '', // 空闲时间
      },
    };
  },
  created() {
    this.fetchUserProfile(); // 组件创建时获取用户资料
  },
  methods: {
    // 获取用户资料
    async fetchUserProfile() {
      try {
        const response = await uni.request({
          url: 'https://734dw56037em.vicp.fun/users/get_user_profile/',
          method: 'GET',
          header: {
            'Authorization': `Token ${uni.getStorageSync('authToken')}`,
            'Content-Type': 'application/json',
          },
        });

        if (response.statusCode === 200) {
          const userData = response.data;
          this.form.name = userData.name;
          this.form.school = userData.school;
          this.avatar = userData.avatar; // 更新头像
        } else {
          uni.showToast({
            title: '获取用户资料失败',
            icon: 'none',
          });
        }
      } catch (error) {
        console.error('获取用户资料错误:', error);
      }
    },
    // 切换编辑状态
    toggleEdit(field) {
      this.editField = this.editField === field ? '' : field;
    },
    // 上传头像
    uploadAvatar() {
      uni.chooseImage({
        count: 1,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success: (res) => {
          const tempFilePath = res.tempFilePaths[0];
          // 这里可以上传到服务器并获取URL
          this.avatar = tempFilePath; // 更新头像
		  console.log(this.avatar);
        },
        fail: () => {
          uni.showToast({
            title: '取消上传',
            icon: 'none',
          });
        },
      });
    },
    // 确认修改
    async confirmEdit() {
      try {
        // 先上传头像
        const uploadResponse = await uni.uploadFile({
          url: 'https://734dw56037em.vicp.fun/users/upload_avatar/',  // 上传头像的接口
          filePath: this.avatar,  // 上传的图片文件路径
          name: 'avatar',  // 对应后端接收的文件字段名
          header: {
            'Authorization': `Token ${uni.getStorageSync('authToken')}`,  // Token 验证
          },
        });
    
        if (uploadResponse.statusCode !== 200) {
          uni.showToast({
            title: '头像上传失败',
            icon: 'none',
          });
          return;  // 如果头像上传失败，直接返回不进行后续操作
        }
    
    
        // 上传其他个人信息
        const response = await uni.request({
          url: 'https://734dw56037em.vicp.fun/users/update_profile/',  // 更新用户信息的接口
          method: 'POST',
          data: {
            major: this.form.major,
            phone: this.form.phone,
            interests: this.form.interests,
            available_time: this.form.freeTime,
          },
          header: {
            'Authorization': `Token ${uni.getStorageSync('authToken')}`,
            'Content-Type': 'application/json',
          },
        });
    
        if (response.statusCode === 200) {
          uni.showToast({
            title: '修改成功',
            icon: 'success',
          });
          
          // 修改成功后返回到个人资料页面
          setTimeout(() => {
            uni.navigateBack();  // 返回上一个页面
          }, 1500);  // 延迟返回，给用户展示修改成功的提示时间
        } else {
          uni.showToast({
            title: '修改失败',
            icon: 'none',
          });
        }
      } catch (error) {
        console.error('提交修改错误:', error);
        uni.showToast({
          title: '网络错误',
          icon: 'none',
        });
      } finally {
        this.editField = '';  // 重置编辑状态
      }
    }
  },
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
  min-height: 100vh;
  box-sizing: border-box;
}

/* 头像部分 */
.avatar-section {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 60px;
  border: 3px solid #ffffff;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  object-fit: cover;
  transition: transform 0.3s;
}

.avatar:hover {
  transform: scale(1.05);
}

/* 个人信息部分 */
.info-section {
  flex: 1;
  margin-bottom: 20px;
}

.info-item {
  display: flex;
  align-items: center;
  padding: 10px 15px;
  margin-bottom: 12px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  transition: background-color 0.3s, box-shadow 0.3s;
}

.info-item:hover {
  background-color: #f9fafb;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.label {
  width: 90px;
  font-size: 16px;
  color: #333333;
}

.value {
  flex: 1;
  font-size: 16px;
  color: #555555;
}

.input {
  flex: 1;
  border: none;
  border-bottom: 1px solid #cccccc;
  padding: 5px 0;
  font-size: 16px;
  outline: none;
  transition: border-bottom 0.3s;
}

.input:focus {
  border-bottom: 2px solid #34C759;
}

.picker {
  flex: 1;
  font-size: 16px;
  color: #555555;
  padding: 5px 0;
}

/* 确认修改按钮 */
.button-container {
  width: 100%;
  padding: 10px 0;
}

.confirm-button {
  width: 100%;
  padding: 15px;
  background: linear-gradient(45deg, #34C759, #30B14C);
  color: #ffffff;
  font-size: 18px;
  border: none;
  border-radius: 30px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: background 0.3s, transform 0.2s;
}

.confirm-button:active {
  background: linear-gradient(45deg, #30B14C, #34C759);
  transform: scale(0.98);
}
</style>
