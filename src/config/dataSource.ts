import { DataSource } from 'typeorm';
import { AlertEvent } from '../entities/alert-event.entity';
import { AlertRequest } from '../entities/alert-request.entity';
import * as dotenv from 'dotenv';

dotenv.config();

export const AppDataSource = new DataSource({
  type: 'postgres',
  host: process.env.DATABASE_HOST,
  port: parseInt(process.env.DATABASE_PORT as string),
  username: process.env.DATABASE_USER,
  password: process.env.DATABASE_PASSWORD,
  database: process.env.DATABASE_NAME,
  entities: [AlertEvent, AlertRequest],
  migrations: ['src/migrations/*.ts'],
  synchronize: false,
});
