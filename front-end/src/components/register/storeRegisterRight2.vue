<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeRegisterRight2"
    >
      <el-form-item class = "storeRegisterRightItem">

        <el-upload
            class="avatar-uploader"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
        >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="license-uploader-icon"><Plus /></el-icon>
        </el-upload>

        <p class = "uploadDetail">上传营业执照</p>

      
      </el-form-item>

    
    </el-form>
</template>

<script>

//   import { ref } from 'vue'
//   import { ElMessage } from 'element-plus'
//   import { Plus } from '@element-plus/icons-vue'
  
//   import type { UploadProps } from 'element-plus'
  
//   const imageUrl = ref('')
  
//   const handleAvatarSuccess: UploadProps['onSuccess'] = (
//     response,
//     uploadFile
//   ) => {
//     imageUrl.value = URL.createObjectURL(uploadFile.raw!)
//   }
  
//   const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
//     if (rawFile.type !== 'image/jpeg') {
//       ElMessage.error('Avatar picture must be JPG format!')
//       return false
//     } else if (rawFile.size / 1024 / 1024 > 2) {
//       ElMessage.error('Avatar picture size can not exceed 2MB!')
//       return false
//     }
//     return true
//   }


</script>






<style>

  .avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }

  .storeRegisterRight2 {
    width: 400px;
    height: 350px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  

  }
  .storeRegisterRightItem {
    margin-top: 0%;
    margin-left: 20%;
    
  }

  .uploadDetail {
    text-align: center;
    font-size: 18px;
    margin-left:20%;
    font-weight: bold;
    color:#606266;
  }

    .avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
  }
  
  .avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
  }
  
  .el-icon.license-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 250px;
    height: 300px;
    text-align: center;
  }
  
</style>

  