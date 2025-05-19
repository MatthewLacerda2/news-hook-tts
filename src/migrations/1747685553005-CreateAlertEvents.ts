import { MigrationInterface, QueryRunner } from "typeorm";

export class CreateAlertEvents1747685553005 implements MigrationInterface {
    name = 'CreateAlertEvents1747685553005'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "alert_events" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "createdAt" TIMESTAMP NOT NULL DEFAULT now(), "payload" jsonb NOT NULL, CONSTRAINT "PK_f8dd833a0534d3a01e8d01e3bca" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "alerts" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "prompt" text NOT NULL, "http_method" character varying NOT NULL, "http_url" character varying NOT NULL, "http_headers" jsonb, "llm_model" character varying, "is_recurring" boolean NOT NULL, "payload_format" jsonb, "max_datetime" TIMESTAMP, "created_at" TIMESTAMP NOT NULL DEFAULT now(), CONSTRAINT "PK_60f895662df096bfcdfab7f4b96" PRIMARY KEY ("id"))`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`DROP TABLE "alerts"`);
        await queryRunner.query(`DROP TABLE "alert_events"`);
    }

}
