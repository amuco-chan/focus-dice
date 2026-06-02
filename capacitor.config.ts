import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.focusdice.app',
  appName: 'Focus Dice',
  webDir: 'www',
  server: {
    androidScheme: 'https'
  }
};

export default config;
