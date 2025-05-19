import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { getDatabaseConfig } from './config/database.config';
import { AlertEvent } from './entities/alert-event.entity';
import { AlertEventsController } from './controllers/alerts-events.controller';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true, // Make config globally available
      envFilePath: '.env',
    }),
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: getDatabaseConfig,
      inject: [ConfigService],
    }),
    TypeOrmModule.forFeature([AlertEvent]),
  ],
  controllers: [AppController, AlertEventsController],
  providers: [AppService],
})
export class AppModule {}
