from sim_pipeline.Pipelines.skypy_pipeline import SkyPyPipeline
from astropy.cosmology import LambdaCDM, FlatwCDM, w0waCDM


class TestSkyPyPipeline(object):
    def setup_method(self):
        from astropy.units import Quantity

        sky_area = Quantity(value=0.05, unit="deg2")
        self.pipeline = SkyPyPipeline(skypy_config=None, sky_area=sky_area)

    def test_cosmology_initialization(self):
        # LambdaCDM model
        cosmo1 = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)
        pipeline1 = SkyPyPipeline(cosmo=cosmo1)
        blue_galaxies = pipeline1.blue_galaxies
        assert blue_galaxies[0]["z"] > 0

        cosmo2 = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)
        pipeline2 = SkyPyPipeline(cosmo=cosmo2)
        red_galaxies = pipeline2.red_galaxies
        assert red_galaxies[0]["z"] > 0

        # FlatwCDM model
        cosmo3 = FlatwCDM(H0=70, Om0=0.3, w0=-1.0)
        pipeline3 = SkyPyPipeline(cosmo=cosmo3)
        red_galaxies = pipeline3.red_galaxies
        assert red_galaxies[0]["z"] > 0

        # w0waCDM model
        cosmo4 = w0waCDM(H0=70, Om0=0.3, Ode0=0.7, w0=-1.0, wa=0.0)
        pipeline4 = SkyPyPipeline(cosmo=cosmo4)
        blue_galaxies = pipeline4.blue_galaxies
        assert blue_galaxies[0]["z"] > 0

    def test_blue_galaxies(self):
        blue_galaxies = self.pipeline.blue_galaxies
        assert blue_galaxies[0]["z"] > 0

    def test_red_galaxies(self):
        red_galaxies = self.pipeline.red_galaxies
        assert red_galaxies[0]["z"] > 0
