from textsummariser.pipeline.stage1data_ingestion import DataIngestionTrainingPipeline
from textsummariser.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info({STAGE_NAME})
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("COMPLETED")
except Exception as e:
        logger.exception(e)
        raise e 